const IP_TO_COPY = "51.83.184.222:25636";

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
