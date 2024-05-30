document.getElementById('generateBlogButton').addEventListener('click', async () => {
        

    const youtubeLink = document.getElementById('youtubeLink').value;
    const blogContent = document.getElementById('blogContent');
    
    if(youtubeLink) {
        document.getElementById('loading-circle').style.display = 'block';
        
        blogContent.innerHTML = ''; // Clear previous content

        const endpointUrl = '/generate-blog';
        
        try {
            const response = await fetch(endpointUrl, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ link: youtubeLink })
            });

            const data = await response.json();

            blogContent.innerHTML = data.content;

        } catch (error) {
            console.error("Error occurred:", error);
            alert("Le blog n'est pas encore oppérationnel, réséyez plus tard.");
            
        }
        document.getElementById('loading-circle').style.display = 'none';
    } else {
        alert("Veuillez insérer un lien youtube.");
    }
});