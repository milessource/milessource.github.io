// id's -> download_modpack | copy_ip | join_discord

const IP_TO_COPY = "x.y.z.w:xxxx";

document.getElementById('join_discord').addEventListener('click', () => {
    window.location.replace('http://miless.duckdns.org/discord');
});

document.getElementById('copy_ip').addEventListener('click', async () => {
    try { await navigator.clipboard.writeText(IP_TO_COPY); } 
    catch (err) { console.error('Error copy to clipboard -> ', err); }
});
