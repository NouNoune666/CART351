

window.onload = function () {
    console.log("js is up and running");
    document
        .querySelector("#insertImageForm")
        .addEventListener("submit", async function (event) {
            event.preventDefault();
            console.log("cat submitted")

            let form = document.querySelector("#insertImageForm")
            let data = new FormData(form)
            try {
                let res = await fetch("/thank_form_two", {
                    method: "POST",
                    body: data,
                });
                let resJSON = await res.json();
                console.log(resJSON);
                document.querySelector("#result-container").innerHTML =
                    `<p>Thanks for submitting your cat!</p>
           <img src="/static/uploads/${resJSON.filename}">`;

            } catch (err) {
                console.log(err);
            }
        })


};
