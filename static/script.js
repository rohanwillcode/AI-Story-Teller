async function generateStory() {
    // Get the user's prompt and the story display area.
    const prompt = document.getElementById("prompt").value;
    const storyDiv = document.getElementById("story");

    // Display a loading message while the story is being generated.
    storyDiv.innerHTML = "⏳ Generating your story...";

    try {
        // Send a POST request to the Flask backend with the user's prompt.
        const response = await fetch("/generate_story", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ prompt: prompt })
        });

        // Parse the JSON response.
        const data = await response.json();

        // Check if the response contains the story.
        if (data.story) {
            // Display the generated story on the page.
            storyDiv.innerHTML = `<h3 class="text-3xl font-bold mb-4">Your Story:</h3><p>${data.story.replace(/\n/g, '<br><br>')}</p>`;
        } else {
            // If there was an error, display the error message.
            storyDiv.innerHTML = `<p class="text-red-500 font-bold">❌ ${data.error || "Something went wrong!"}</p>`;
        }
    } catch (error) {
        // Catch any network or other errors and display them.
        storyDiv.innerHTML = `<p class="text-red-500 font-bold">❌ Error: ${error.message}</p>`;
    }
}
