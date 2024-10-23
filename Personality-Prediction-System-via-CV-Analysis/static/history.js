// In history.js
document.addEventListener('DOMContentLoaded', function() {
    fetch('/history')
        .then(response => response.json())
        .then(data => {
            displayContactInfo(data.contactInfo);
            displayEducation(data.education);
            displayWorkExperience(data.workExperience);
            displaySkills(data.skills);
            displayPersonalityTraits(data.personalityTraits);
            displayAIPrediction(data.aiPrediction);
        })
        .catch(error => console.error('Error fetching history:', error));
});

function displayContactInfo(data) {
    const container = document.getElementById('contactInfoContainer');
    const table = createTable(['Name', 'Email', 'Phone']);
    data.forEach(item => {
        const row = createRow([item.name, item.email, item.phone]);
        table.appendChild(row);
    });
    container.appendChild(table);
}

function displayEducation(data) {
    const container = document.getElementById('educationContainer');
    const table = createTable(['Institution', 'Degree', 'Year']);
    data.forEach(item => {
        const row = createRow([item.institution, item.degree, item.year]);
        table.appendChild(row);
    });
    container.appendChild(table);
}

function displayWorkExperience(data) {
    const container = document.getElementById('workExperienceContainer');
    const table = createTable(['Company', 'Position', 'Years']);
    data.forEach(item => {
        const row = createRow([item.company, item.position, item.years]);
        table.appendChild(row);
    });
    container.appendChild(table);
}

function displaySkills(data) {
    const container = document.getElementById('skillsContainer');
    const table = createTable(['Skill', 'Proficiency']);
    data.forEach(item => {
        const row = createRow([item.skill, item.proficiency]);
        table.appendChild(row);
    });
    container.appendChild(table);
}

function displayPersonalityTraits(data) {
    const container = document.getElementById('personalityTraitsContainer');
    const table = createTable(['Trait', 'Description']);
    data.forEach(item => {
        const row = createRow([item.trait, item.description]);
        table.appendChild(row);
    });
    container.appendChild(table);
}

function displayAIPrediction(data) {
    const container = document.getElementById('aiPredictionContainer');
    const table = createTable(['Prediction', 'Confidence Level']);
    data.forEach(item => {
        const row = createRow([item.prediction, item.confidenceLevel]);
        table.appendChild(row);
    });
    container.appendChild(table);
}

function createTable(headers) {
    const table = document.createElement('table');
    const thead = document.createElement('thead');
    const headerRow = document.createElement('tr');

    headers.forEach(header => {
        const th = document.createElement('th');
        th.textContent = header;
        headerRow.appendChild(th);
    });

    thead.appendChild(headerRow);
    table.appendChild(thead);
    table.appendChild(document.createElement('tbody')); // Create an empty tbody
    return table;
}

function createRow(data) {
    const row = document.createElement('tr');
    data.forEach(cellData => {
        const td = document.createElement('td');
        td.textContent = cellData;
        row.appendChild(td);
    });
    return row;
}
