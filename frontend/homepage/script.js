const url = "https://health-risk-prediction-9qe8.onrender.com/get_info"


const diseaseContainer = document.getElementById("diseaseCards");


function createDiseaseCard(name, details){

    const card = document.createElement("div");
    card.className = "disease-card";

    card.innerHTML = `
        <div class="disease-header">
            <span>${name}</span>
            <span>+</span>
        </div>

        <div class="disease-body">
            <p>${details}</p>
        </div>
    `;

    card.querySelector(".disease-header").addEventListener("click",()=>{

        card.classList.toggle("active");

        const sign = card.querySelector(".disease-header span:last-child");

        sign.textContent = card.classList.contains("active") ? "−" : "+";

    });

    diseaseContainer.appendChild(card);

}



function show_health_cards(data){
    console.log(data["models"])

    for( model in data["models"] ) {
        let name = data['models'][model]['name']
        let details = data['models'][model]['details']
        
        name = name.toUpperCase().replaceAll("_", " ")

        createDiseaseCard(name, details)

    }
}

function scrollToAbout() {
    document.getElementById("about").scrollIntoView({
        behavior: "smooth",
        block: "start"
    });
}





fetch(url)
  .then(response => {
    if (!response.ok) {
      throw new Error(`HTTP error! Status: ${response.status}`);
    }
    return response.json();
  })
  .then(data => {
    show_health_cards(data);
  })
  .catch(error => {
    console.error('Fetch failed:', error);
  });


document.getElementById("mail").addEventListener("click", (e)=>{
    window.location.href = "mailto:ansariayaan0604@gmail.com"
})