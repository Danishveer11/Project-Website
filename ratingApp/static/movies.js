document.addEventListener("DOMContentLoaded", function() {
  

document.getElementById("MovieForm").addEventListener("submit", function(e) {
    e.preventDefault(); // Prevent form from reloading page

    const rating = document.getElementById("rating").value;
    const reviewText = document.getElementById("reviewInput").value;

    if (!rating || !reviewText.trim()) {
        alert("Please select a rating and write a review.");
        return;
    }

    // Create new review
    const reviewDiv = document.createElement("div");
    reviewDiv.className = "review";

    const header = document.createElement("h4");
    header.textContent = `You ⭐ ${rating}/10`;

    const paragraph = document.createElement("p");
    paragraph.textContent = reviewText;

    const deleteBtn = document.createElement("button");
    deleteBtn.textContent = "Delete";
    deleteBtn.className="Delete_btns";
    deleteBtn.addEventListener("click", () => reviewDiv.remove());

    reviewDiv.appendChild(header);
    reviewDiv.appendChild(paragraph);
    reviewDiv.appendChild(deleteBtn);

    // Append to reviews container (new or top)
    const reviewsContainer = document.getElementById("reviews-container");
    reviewsContainer.insertBefore(reviewDiv, reviewsContainer.firstChild);

    // Clear inputs
    document.getElementById("reviewInput").value = "";
    document.getElementById("rating").value = "";
}); });
