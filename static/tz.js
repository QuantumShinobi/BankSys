function detectTimezone() {
  const timezone = Intl.DateTimeFormat().resolvedOptions().timeZone;
  // Send the timezone to the server using an AJAX request or other methods
  // For example, you can use the Fetch API or jQuery's $.ajax
  // Here's a simple Fetch example:
  fetch("/set_timezone/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-CSRFToken": "{{ csrf_token }}", // Ensure CSRF token is included
    },
    body: JSON.stringify({ timezone }),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log(data.message);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}
document.addEventListener("DOMContentLoaded", () => {
  detectTimezone();
});
