```bash
## Understanding Connection Methods

**MAC Address Login**  
Used when the router has no IP configuration, the IP is unknown, or the device becomes unreachable due to misconfiguration. WinBox communicates over Layer 2, allowing direct access within the same broadcast domain regardless of IP settings. This method is ideal for initial provisioning, recovery scenarios, and situations where L3 connectivity is not yet available.

**IP Address Login**  
The standard operational method once the router is properly configured. IP-based access provides stable Layer 3 connectivity, supports remote management across different subnets, and aligns with production environments where routing, VLANs, and access control are enforced. This approach is required for any scalable or remotely managed deployment.
