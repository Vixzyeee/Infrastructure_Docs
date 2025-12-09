
Secara teknis sih valid, tapi visual preview-nya amburadul.

**Solusi:**  
Tetap pakai H1, H2, H3 tapi pastikan hierarchy-nya konsisten.  
Format yang gua kasih itu udah clean buat dokumentasi teknis.

---

## 5. **Ini versi final yang udah gue poles + detail rapi**

Silakan lu lihat ini, udah perfect buat GitHub:

---

```md
# RouterBOARD-1 Configuration

## Connect to RouterBOARD-1 via MAC Address
- Connect to: **`<ROUTER_MAC_ADDRESS>`**  
  Example: `00:0C:42:FA:60:FC`
- Login: **`<ROUTER_USERNAME>`**  
  Example: `admin`
- Password: **`<ROUTER_PASSWORD>`**  
  Example: (leave blank if default)

---

## Configure IP Address (RouterBOARD-1 to PC-1)

### MikroTik Command
```bash
/ip address add address=<ROUTERBOARD_IP_TO_PC1> interface=<INTERFACE_TO_PC1>
# Example
/ip address add address=192.168.88.1/24 interface=ether5
