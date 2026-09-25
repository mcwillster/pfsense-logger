const PFSENSE_IP = "192.168.1.1";

browser.cookies.onChanged.addListener((changeInfo) => {
    const cookie = changeInfo.cookie;

    if (cookie.domain.includes(PFSENSE_IP) && cookie.name === "PHPSESSID" && !changeInfo.removed) {
        const sessionId = cookie.value;
        const timestamp = new Date().toLocaleTimeString();
        console.log(`[${timestamp}] pfSense Login Detected! Session ID: ${sessionId}`);
        
        // Send the ID to your local Python server
        fetch("http://localhost:8000", {
            method: "POST",
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            },
            body: `session=${encodeURIComponent(sessionId)}`
        }).catch(err => console.error("Python logger not running.", err));
    }
});