// Update this if your pfSense router is on a different IP
const PFSENSE_IP = "192.168.1.1";

browser.cookies.onChanged.addListener((changeInfo) => {
    const cookie = changeInfo.cookie;

    // Check if the cookie belongs to pfSense and is the session cookie
    if (cookie.domain.includes(PFSENSE_IP) && cookie.name === "PHPSESSID") {
        
        // Ensure we are catching a new/updated cookie, not a deletion (logout)
        if (!changeInfo.removed) {
            const sessionId = cookie.value;
            const timestamp = new Date().toLocaleTimeString();
            
            console.log(`[${timestamp}] pfSense Login Detected! Session ID: ${sessionId}`);
            
            // Optional: You can also trigger a browser notification
            // browser.notifications.create({
            //     type: "basic",
            //     title: "pfSense Session Logged",
            //     message: `ID: ${sessionId}`
            // });
        }
    }
});