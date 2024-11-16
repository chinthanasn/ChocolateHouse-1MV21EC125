const baseUrl = "http://127.0.0.1:5000";

document.getElementById('addFlavour').addEventListener('click', function () {
    let name = prompt("Enter the name of the new flavour:");
    let season = prompt("Enter the season for this flavour:");
    let availability = prompt("Is this flavour available? (1 for Yes, 0 for No):");

    if (name && season && availability !== null) {
        fetch(`${baseUrl}/flavours`, {
            method: 'POST',
            mode: 'cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ name, season, availability: parseInt(availability) })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultContainer').innerHTML = data.message || data.error;
        })
        .catch(error => {
            document.getElementById('resultContainer').innerHTML = `Error: ${error}`;
        });
    }
});

document.getElementById('getFlavour').addEventListener('click', function () {
    fetch(`${baseUrl}/flavours`,{
        mode: 'cors',
    })
        .then(response => response.json())
        .then(data => {
            let output = '<ul>';
            data.forEach(flavour => {
                output += `<li>${flavour.name} (${flavour.season}) - ${flavour.availability ? "Available" : "Unavailable"}</li>`;
            });
            output += '</ul>';
            document.getElementById('resultContainer').innerHTML = output;
        })
        .catch(error => {
            document.getElementById('resultContainer').innerHTML = `Error: ${error}`;
        });
});

document.getElementById('addInventory').addEventListener('click', function () {
    let ingredient = prompt("Enter the inventory item name:");
    let quantity = prompt("Enter the quantity:");
    let availability = prompt("Is this item available? (1 for Yes, 0 for No):");

    if (ingredient && quantity && availability !== null) {
        fetch(`${baseUrl}/inventory`, {
            method: 'POST',
            mode: 'cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ ingredient, quantity: parseInt(quantity), availability: parseInt(availability) })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultContainer').innerHTML = data.message || data.error;
        })
        .catch(error => {
            document.getElementById('resultContainer').innerHTML = `Error: ${error}`;
        });
    }
});

document.getElementById('getInventory').addEventListener('click', function () {
    fetch(`${baseUrl}/inventory`,{mode: 'cors',})
        .then(response => response.json())
        .then(data => {
            let output = '<ul>';
            data.forEach(item => {
                output += `<li>${item.ingredient}: ${item.quantity} (${item.availability ? "Available" : "Unavailable"})</li>`;
            });
            output += '</ul>';
            document.getElementById('resultContainer').innerHTML = output;
        })
        .catch(error => {
            document.getElementById('resultContainer').innerHTML = `Error: ${error}`;
        });
});

document.getElementById('addAllergies').addEventListener('click', function () {
    let customer_name = prompt("Enter the customer's name:");
    let allergy = prompt("Enter the allergy:");
    let suggestion = prompt("Enter a suggestion for the allergy:");

    if (customer_name && allergy && suggestion) {
        fetch(`${baseUrl}/allergies`, {
            method: 'POST',
            mode: 'cors',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ customer_name, allergy, suggestion })
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('resultContainer').innerHTML = data.message || data.error;
        })
        .catch(error => {
            document.getElementById('resultContainer').innerHTML = `Error: ${error}`;
        });
    }
});

document.getElementById('getAllergies').addEventListener('click', function () {
    let customer_name = prompt("Enter the customer's name:");

    if (customer_name) {
        fetch(`${baseUrl}/allergies/${customer_name}`,{mode: 'cors',})
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    let output = '<ul>';
                    data.forEach(allergy => {
                        output += `<li>${allergy.allergy}: ${allergy.suggestion}</li>`;
                    });
                    output += '</ul>';
                    document.getElementById('resultContainer').innerHTML = output;
                } else {
                    document.getElementById('resultContainer').innerHTML = `No allergies found for ${customer_name}.`;
                }
            })
            .catch(error => {
                document.getElementById('resultContainer').innerHTML = `Error: ${error}`;
            });
    }
});
