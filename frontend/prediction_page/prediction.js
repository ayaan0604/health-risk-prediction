const inputForm = document.getElementById("input-form")
    
const resultDiv = document.getElementById("result")

const url = "http://127.0.0.1:8000/results"

function getRiskLevel(percentage){
    if(percentage < 25) return "Low"

    if(percentage <60) return "Moderate"

    return "High"
}

function getRiskClass(risk){
    if(risk == "High") return "risk-high"
    if(risk == "Moderate") return "risk-moderate"
    return "risk-low"
}

function getDiseaseName(disease ){
    disease = disease.charAt(0).toUpperCase() + disease.slice(1); //capitlize

    return disease.replaceAll("_", " ")
}

function createRiskCard(name, percentage){

    const riskLevel = getRiskLevel(percentage)

    //card header
    const cardHeader = document.createElement("div")
    cardHeader.classList.add("risk-card-header")

    const riskTitle = document.createElement("span")
    riskTitle.classList.add("risk-title")
    riskTitle.textContent = `${getDiseaseName(name)}: ${riskLevel}`
    cardHeader.append(riskTitle)

    const riskDot = document.createElement("span")
    riskDot.classList.add("risk-dot")
    riskDot.classList.add(getRiskClass(riskLevel))

    cardHeader.appendChild(riskDot)
    //card header complete

    //risk card body
    const riskCardBody = document.createElement("div")
    riskCardBody.classList.add("risk-card-body")

    const progressContainer = document.createElement("div")
    progressContainer.classList.add("progress-container")

    const progressBar = document.createElement("div")
    progressBar.classList.add("progress-bar")
    progressBar.classList.add(getRiskClass(riskLevel))
    progressBar.style.width = `${percentage}%`

    progressContainer.appendChild(progressBar)  

    const riskPercentage = document.createElement("span")
    riskPercentage.classList.add("risk-percent")
    riskPercentage.textContent = `${percentage}%`

    riskCardBody.appendChild(progressContainer)
    riskCardBody.appendChild(riskPercentage)
    //risk card body complete

    //main card
    const riskCard = document.createElement("div")
    riskCard.classList.add("risk-card")

    riskCard.appendChild(cardHeader)
    riskCard.appendChild(riskCardBody)

    return riskCard

}

function getFormData(){
    const inputForm = document.getElementById("input-form")

    const formData = Object.fromEntries(new FormData(inputForm))

    return formData
}

function getResponse(data){

    let options = {
        method : "POST",
        headers : {
            "Content-Type" : 'application/json'
        },

        body: JSON.stringify(data)
    }

    fetch(url, options)
    .then((response)=>response.json())
    .then((json)=>displayResult(json))

}

function displayResult(result){

    resultDiv.innerHTML = ""

    //sort in decreasing order of the risk

    const sortedDiseases = Object.entries(result);

    sortedDiseases.sort((a, b) => b[1] - a[1]);

    sortedDiseases.forEach(([disease, percentage]) =>
        {
            
            percentage = (100 * percentage).toFixed(0)

            const riskCard = createRiskCard(disease, percentage)

            resultDiv.appendChild(riskCard)

        }
    )

}

inputForm.addEventListener("submit", (event)=>{
    event.preventDefault()

    resultDiv.innerHTML = ""

    const data = getFormData()

    getResponse(data)


    
})