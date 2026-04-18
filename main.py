import base64

import click

import utils.config as config
import utils.logs as logger
from freebox.auth import FreeboxConnection


@click.group()
@click.option(
    "--address", default="http://mafreebox.freebox.fr", help="Freebox Server Adress"
)
@click.pass_context
def cli(ctx, address):
    ctx.ensure_object(dict)
    ctx.obj["freebox"] = FreeboxConnection(freebox_address=address)
    ctx.obj["freebox"].get_session_token()


@cli.group()
def token():
    pass


@cli.group()
def session():
    pass


@session.command()
@click.pass_context
def test(ctx):
    pass


@session.command()
@click.pass_context
def close(ctx):
    ctx.obj["freebox"].close_session()

    config.Remove("SessionToken", "SessionTokenTime")

    logger.success("✔️  Successfully closed session")


@token.command()
@click.argument("token", nargs=-1)
def set(token):
    config.Edit({"AuthenticationToken": token[0]})
    logger.success(f'✔️  Successfully added token "{token[0]}" to the config')


@token.command()
def clear():
    config.Remove("AuthenticationToken", "SessionToken", "SessionTokenTime")
    logger.success("✔️  Successfully removed token from the config")


@cli.command()
@click.argument("args", nargs=-1)
@click.pass_context
def get(ctx, args):
    res = ctx.obj["freebox"].authenticated_request("/api/v8/lan/config/")["result"]

    logger.present_request(res, filter=args)


@cli.command()
@click.argument("args", nargs=-1)
@click.pass_context
def vm(ctx, args):
    res = ctx.obj["freebox"].authenticated_request("/api/v8/vm/")["result"]

    if not len(args):
        for machine in res:
            logger.show(
                "• ["
                + (
                    machine["name"]
                    if machine["name"]
                    else machine["cloudinit_hostname"]
                )
                + "]"
            )
            for element in machine:
                logger.show(
                    f"   • {element}: {machine[element] if element not in ['disk_path'] else base64.b64decode(machine['disk_path']).decode()}"
                )
        return

    if args[0] not in [element["name"] for element in res]:
        logger.error(f"{args[0]} is not a valid virtual machine")
        return

    for element in res:
        if element["name"] == args[0]:
            logger.present_request(element, filter=args[1:] if len(args) > 1 else [])

    return


@cli.group()
def disk():
    pass


@disk.command()
@click.pass_context
def list(ctx):
    res = ctx.obj["freebox"].authenticated_request("/api/v8/storage/disk/")["result"]

    for disk in res:
        logger.show(
            f"{disk['id']} | {disk['model']} ({disk['total_bytes'] / 1000**3} GB)"
            + (
                " [idle since "
                + (
                    (str(disk["idle_duration"]) + " seconds")
                    if disk["idle_duration"] < 60
                    else (str(disk["idle_duration"] // 60) + " minutes")
                )
                + "]"
                if disk["idle"]
                else ""
            )
        )
        for partition in disk["partitions"]:
            logger.show(
                f"• [{partition['id']}] '{partition['label']}' ({partition['fstype']}, {partition['state']})"
            )
            logger.show(
                f"  Mounted at : {base64.b64decode(partition['path']).decode()}"
            )
            logger.show(
                f"  {partition['used_bytes'] / 1000**3} GB Used / {partition['total_bytes'] / 1000**3} GB Total | {partition['free_bytes'] / 1000**3} GB Free"
            )
        logger.show("")

    return


@disk.command()
@click.argument("args", nargs=-1)
@click.pass_context
def infos(ctx, args):
    if not len(args):
        logger.error("No disk or partition specified")

    res = ctx.obj["freebox"].authenticated_request(f"/api/v8/storage/disk/{args[0]}")[
        "result"
    ]

    logger.present_request(res, args[1:] if len(args) > 1 else [])

    return


if __name__ == "__main__":
    cli()
