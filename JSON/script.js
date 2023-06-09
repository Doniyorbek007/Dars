const root = document.getElementById("root");

fetch("data.json")
    .then(response => response.json())
    .then(data => {
        data.forEach(i => {
            root.innerHTML += `
        <h1>Ishchi nomi: ${i.ishchi_nomi}</h1>
        <p>Ishchi joyi: ${i.ish_joyi}</p>
        <p>Ish vaqti: ${i.ish_vaqti}</p>
        <i>Daromadi: ${i.daromadi}</i>
        `;
        });
    });