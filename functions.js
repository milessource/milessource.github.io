// id's -> download_modpack | copy_ip | join_discord | ip_field

const IP_TO_COPY = "x.y.z.w:xxxx";

document.getElementById('ip_field').value = IP_TO_COPY;

document.getElementById('join_discord').addEventListener('click', () => {
    window.location.replace('http://miless.duckdns.org/discord');
});

document.getElementById('copy_ip').addEventListener('click', async () => {
    const ip_field = document.getElementById('ip_field');
    ip_field.focus(); ip_field.select();
    try { document.execCommand('copy'); } 
    catch (err) {console.error('Unable to copy to clipboard -> ', err); }
});
