export function daddy(url, data, alternate_data) {

    let send_data = {
        "url": url,
        "data": data
    }

    function set_data(resp) {
        let arg

        if (resp['status'] == 200) {
            var req_data = resp['data']
            for (arg of req_data) {
                document.getElementById(arg[0]).innerHTML = arg[1]
            }
        }
        else {
            var val
            console.error('Error:', error, "using alternate data");
            for (val of alternate_data) {
                document.getElementById(val[0]).innerHTML = val[1]
            }
        }
    }

    fetch("http://api.localhost:5000/daddy.js", {

        method: "POST",
        body: JSON.stringify(send_data),
        headers: {
            "Content-type": "application/json; charset=UTF-8"
        }
    })
        .then((response) => response.json())
        .then((json) => set_data(json))
        .catch(error => {
            var val
            console.error('Error:', error, "using alternate data");
            for (val of alternate_data) {
                document.getElementById(val[0]).innerHTML = val[1]
            }
        });
}

