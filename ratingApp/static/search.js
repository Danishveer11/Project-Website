async function searchAPI() {
    // gets Search input
    const query = document.getElementById("SearchInput").value;
    // gets the section tag
    const resultsDiv = document.getElementById("layout");

    // Clear results if query is empty, input should more than 1 character
    if (query.length < 2) {
        
        resultsDiv.innerHTML = "Name should have more than 1 characters";
        return;
    }

    // Call your Django API endpointy
    // url
    const url = `/app/search/api/?q=${encodeURIComponent(query)}`;

    
    try {
        // fetch
        const response = await fetch(url);
        const data = await response.json();

        resultsDiv.innerHTML = ""; // clear previous results
        // list of movies will be stored in lists
        const lists = document.createElement("div");
        lists.className="results"; 
        // loop
        data.results.forEach(movie => {
            // Container to store each movie
            const div = document.createElement("div");
            div.className = "movie_card";

            // Poster
            const poster = document.createElement("div");
            poster.className = "poster";
            if (movie.poster_path) {
                // if movie poster exist then create div and show movie
                const img = document.createElement("img");
                img.src = `https://image.tmdb.org/t/p/w500${movie.poster_path}`;
                img.className = "image";
                poster.appendChild(img);
                div.appendChild(poster);
            }
           
            // Details of movies
            const div_details = document.createElement("div");
            div_details.className = "details";
            // title
            const title = document.createElement("h3");
            title.className = "title";
            title.textContent = `${movie.title} (${movie.release_date?.slice(0, 4) || "N/A"})`;
            div_details.appendChild(title);

            
            div.appendChild(div_details);
            

            // Click to go to detail page
            const link = document.createElement("a");  
            // by clicking on link(div) will take to movie page
            link.href = `/app/movies/${movie.id}`; 
            link.className = "movie_link"
            link.appendChild(div); 
            lists.appendChild(link);
            resultsDiv.appendChild(lists); // append to the section tag

            
        });
        // error
    } catch (error) {
        console.error("Error fetching movies:", error);
        resultsDiv.innerHTML = "<p>Failed to load results.</p>";
    }
}
