const button = document.getElementById("processButton");

button.addEventListener("click", async function () {

    const input = document.getElementById("inputText").value;
    const feature = document.getElementById("feature").value;
    const output = document.getElementById("output");

    if (input.trim() === "") {
        output.textContent = "Please enter some text first.";
        return;
    }

    if (feature !== "simplify") {
        output.textContent =
            "This feature will be added in the next development stage.";
        return;
    }

    output.textContent = "Processing...";

    try {

        const response = await fetch("http://127.0.0.1:5000/simplify", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                text: input
            })
        });

        const data = await response.json();

        if (!response.ok) {
            output.textContent = data.error || "Something went wrong.";
            return;
        }

        output.textContent = data.simplified;

    } catch (error) {

        console.error(error);

        output.textContent =
            "Could not connect to the backend. Make sure the Flask server is running.";
    }
});