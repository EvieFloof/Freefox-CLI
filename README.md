<!--suppress ALL -->

<div align="center">
  <img width="153" height="153" alt="BrokeOut Logo" src="https://github.com/user-attachments/assets/fc39645a-1f39-4aaa-9871-7055346d91a5" />

  <h1>FreeFox</h1>
  <h3>An easy-to-use CLI Interface to manage your Freebox V7+</h3>
  
  <p>
    <a href="#-about">About</a> • 
    <a href="#-installation">Installation</a> • 
    <a href="#-roadmap">Roadmap</a> • 
    <a href="#-faq">FAQ</a>
  </p>
</div>

---

## 📖 About

**FreeFox CLI** is a Python based CLI tool to manage FreeboxOS, the system running on ISP Routers provided by Free SAS.  

---

## 🚀 Installation

### 🧩 Prerequisites
- Python **3.8+**
- [`uv`](https://github.com/astral-sh/uv) package manager

### ⚙️ Quick Start
```bash
# Clone the repository
git clone https://github.com/EvieFloof/ffox

# Navigate to the project directory
cd ffox

# Sync dependencies
uv sync

# Install Freefox
uv tool install .

# Run the cli
ffox session test

```

---

## 📸 Roadmap

- [x] Good-looking CLI interface
- [x] Login and create token to access the Freebox

### APIs

**AirMedia**
- [ ] Air Media API

**Call / Contaxts**
- [ ] Call API
- [ ] Voicemail API
- [ ] Contacts API

**Configuration**
- [ ] Connection API
- [ ] LAN Config API
- [ ] Lan Browser API
- [ ] Wake On LAN API
- [ ] FreePlug API
- [ ] DHCP
    - [ ] DHCP Configuration API
    - [ ] DHCP Static Lease API
- [ ] DHCPv6 Configuration API
- [ ] FTP Config API
- [ ] TFTP Config API
- [ ] DMZ Config API
- [ ] Port Forwarding API
- [ ] Incoming Port API
- [ ] UPnP IGD
    - [ ] UPnP IGD Config API
    - [ ] UPnP IGD Redirection API
- [ ] LCD Config API
- [ ] LedStrip API
- [ ] Network Share
    - [ ] Samba Config API
    - [ ] AFP Config API
- [ ] UPnP AV Config API
- [ ] Switch API
- [ ] WiFi
    - [ ] WiFi Global Config API
    - [ ] WiFi Global State API
    - [ ] WiFi AP API
    - [ ] WiFi BSS API
    - [ ] WiFi Radar API
    - [ ] WiFi Planning API
    - [ ] WiFi MAC Filter API
    - [ ] WiFi Config Reset API
    - [ ] WiFi Diagnistic API
    - [ ] WiFi WPS API
    - [ ] WiFi Guest API
    - [ ] WiFi Temporary Disable API
    - [ ] WiFi MLO API
- [ ] System API
- [ ] VPN Server API
    - [ ] VPN Server Config API
    - [ ] VPN Server User API
    - [ ] VPN Server Connection API
    - [ ] VPN User Configuration File API
- [ ] Slowness API
- [ ] Downloads API
    - [ ] Download Stats API
    - [ ] Download Files API
    - [ ] Download Trackers API
    - [ ] Download Peers API
    - [ ] Download Pieces API
    - [ ] Download Blacklist API
    - [ ] Donwload Feeds API
    - [ ] Download Configuration API
- [ ] File System API
    - [ ] File Sharing Link API
    - [ ] File Upload API
        - [ ] WebSocket File Upload API
        - [ ] Upload Progress Tracking API
- [ ] Home
    - [ ] Home API
    - [ ] Cameras API
- [ ] Language API
- [ ] Notification API
- [ ] Parental Filter
    - [ ] Profiles API
    - [ ] Network Control API
    - [ ] Rule API
- [ ] Player API
- [ ] PVR
    - [ ] PVR Config API
    - [ ] PVR Quota API
    - [ ] PVR Precord API
    - [ ] PVR Frecord API
    - [ ] Storage Media API
- [ ] RRD
- [ ] Standby API
- [ ] Storage
    - [ ] Storage Disk API
    - [ ] Storage Partition API
    - [ ] Storage Config API
- [ ] RAID API
- [ ] SFP API
- [ ] Update API
- [ ] Virtual Machine API

---
---

## ❓ FAQ

<details>
<summary><b>What's the current state of `ffox` ?</b></summary>
Currently in a very barebone phase! Basic things works but that's it.
</details>

<details>
<summary><b>Why did you create this ?</b></summary>
I really enjoy Free SAS products, and I like CLIs :D
</details>

<details>
<summary><b>Can I contribute to the project ?</b></summary>
Of course you can, just open a pull request
</details>

<details>
<summary><b>What platforms does it support ?</b></summary>
Built with Python, `ffox` is Cross-Platform
</details>

<details>
<summary><b>Is it free ?</b></summary>
Absolutely! `ffox` is and always will be **free and open source**.
</details>

<details>
<summary><b>Why "FreeFox"</b></summary>
Cause I reeeally like foxes :3
</details>

---

## 💬 Feedback & Support

We’d love to hear from you!
Whether you found a bug, have an idea, or just want to say hi:

* 📧 **Email:** [contactme@cutefox.dev](mailto:contactme@cutefox.dev)
* 🐛 **Report bugs:** [GitHub Issues](https://www.github.com/EvieFloof/Freefox-CLI/issues)
* ⭐ **Like the project?** Give it a star on GitHub!

---

## 🙏 Acknowledgments

* 🕹️ Thanks to Free SAS for the Freebox Delta
* ❤️ Special thanks to our testers and early supporters

---

<div align="center">

**Made with ❤️ and lots of API Calls**

⬆ [Back to Top](#readme)

</div>
