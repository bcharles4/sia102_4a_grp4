let monthlyIllnessChart;
let mortalityData = {};
let currentYear = 2024; // Default year
let illnessData; // Declare data globally

// Define a fixed color palette
const colorPalette = [
    "#FF5733", "#33FF57", "#3357FF", "#F39C12", "#8E44AD",
    "#FFC300", "#DAF7A6", "#C70039", "#900C3F", "#581845"
];

// Toggle chart visibility based on selection
function showChart(chartId) {
    document.querySelectorAll('.chart-container').forEach(chart => {
        chart.style.display = 'none';
    });
    if (chartId) {
        document.getElementById(chartId).style.display = 'flex';
    }
}

document.getElementById('chartSelectionDropdown').onchange = function () {
    const selectedValue = this.value;
    showChart(selectedValue);
};


// Initialize page with default chart
document.addEventListener('DOMContentLoaded', () => {
    const defaultChartId = 'illness-chart';
    document.getElementById('chartSelectionDropdown').value = defaultChartId; // Preselect the dropdown
    showChart(defaultChartId); // Show the default chart

    // Illness Distribution Pie Chart
    const ctxIllness = document.getElementById('illnessPieChart').getContext('2d');

    const illnessPieChart = new Chart(ctxIllness, {
        type: 'pie',
        data: {
            labels: [],  // Will be populated dynamically
            datasets: [{
                label: 'Illnesses',
                data: [],
                backgroundColor: ['#A8DADC', '#FFE156', '#6A4C93', '#FF6B6B', '#F4A261'],
                borderColor: ['#457B9D', '#FFD23F', '#4F2C91', '#F14657', '#F1A15B'],
                borderWidth: 1
            }]
        },
        options: {
            responsive: true,
            aspectRatio: 1.5,
            plugins: {
                legend: { position: 'top' }
            },
            animation: false
        }
    });

    // Fetch data from the Django API endpoint
    fetch('/get_illness_data')
        .then(response => response.json())
        .then(data => {
            if (data.illness_data) {
                illnessPieChart.data.labels = data.illness_data.labels;
                illnessPieChart.data.datasets[0].data = data.illness_data.data;
                illnessPieChart.update();
            } else {
                console.error("No illness data found");
            }
        })
        .catch(error => console.error("Error fetching illness data:", error));
});

// Populate and set up the year dropdown for the Mortality Rate chart
function setupMortalityYearDropdown() {
    const dropdown = document.getElementById('mortalityYearDropdown');
    const availableYears = Object.keys(mortalityData).map(Number);

    // Populate the dropdown
    availableYears.forEach(year => {
        const option = document.createElement('option');
        option.value = year;
        option.textContent = year;
        dropdown.appendChild(option);
    });

    // Set default value
    dropdown.value = currentYear;

    // Update the chart when a new year is selected
    dropdown.onchange = function () {
        currentYear = parseInt(this.value, 10);
        updateMortalityChart(currentYear);
    };
}

// Fetch and initialize the Mortality Rate chart
fetch('/mortality_data/')
    .then(response => response.json())
    .then(data => {
        mortalityData = data; // Store the fetched data
        setupMortalityYearDropdown(); // Set up the dropdown
        updateMortalityChart(currentYear); // Initialize the chart with the default year
    })
    .catch(error => console.error('Error fetching mortality data:', error));

// Initialize the Mortality Rate chart
const ctxMortality = document.getElementById('mortalityBarChart').getContext('2d');
const mortalityBarChart = new Chart(ctxMortality, {
    type: 'bar',
    data: {
        labels: [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ],
        datasets: [{
            label: 'Number of Deaths',
            data: [], // Filled dynamically
            backgroundColor: '#4A90E2',
            borderColor: '#3B7AC4',
            borderWidth: 1
        }]
    },
    options: {
        responsive: true,
        scales: {
            y: { beginAtZero: true }
        },
        plugins: {
            legend: { position: 'top' }
        }
    }
});

// Function to update the Mortality Rate chart
function updateMortalityChart(year) {
    const dataForYear = mortalityData[year] || [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0];
    mortalityBarChart.data.datasets[0].data = dataForYear;
    mortalityBarChart.update();
}

// Fetch and display Illness Deaths Bar Chart
fetch('/illness_deaths_data/')
    .then(response => response.json())
    .then(data => {
        const labels = Object.keys(data);
        const deathCounts = Object.values(data);

        const ctxDeaths = document.getElementById('illnessDeathsChart').getContext('2d');
        new Chart(ctxDeaths, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Deaths',
                    data: deathCounts,
                    backgroundColor: '#F14657',
                    borderColor: '#F13647',
                    borderWidth: 1
                }]
            },
            options: {
                responsive: true,
                scales: {
                    y: { beginAtZero: true }
                },
                plugins: {
                    legend: { position: 'top' }
                }
            }
        });
    })
    .catch(error => console.error('Error fetching illness deaths data:', error));

// Helper function to generate datasets for a specific year
const getDatasetsForYear = (year, illnessData) => {
    return Object.keys(illnessData)
        .map((illness, index) => ({
            label: illness,
            data: illnessData[illness][year] || [],
            borderColor: colorPalette[index % colorPalette.length], // Assign a color based on index
            fill: false
        }))
        .filter(dataset => dataset.data.some(value => value > 0)); // Only include illnesses with data > 0
};

// Initialize the Monthly Illness Distribution chart
const initializeChart = (data) => {
    const labels = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ];

    const ctxMonthlyIllness = document.getElementById('monthlyIllnessLineChart').getContext('2d');
    const chart = new Chart(ctxMonthlyIllness, {
        type: 'line',
        data: {
            labels: labels,
            datasets: getDatasetsForYear(currentYear, data)
        },
        options: {
            responsive: true,
            plugins: {
                legend: { position: 'top' }
            },
            scales: {
                y: { beginAtZero: true }
            },
            animation: false // Disable animation for updates
        }
    });

    return chart;
};

// Fetch and initialize the Monthly Illness Distribution chart
fetch('/monthly_illness_distribution/')
    .then(response => response.json())
    .then(fetchedData => {
        illnessData = fetchedData; // Assign the fetched data to the global variable
        monthlyIllnessChart = initializeChart(illnessData);

        // Populate and set up the year dropdown for the Monthly Illness chart
        const setupIllnessYearDropdown = () => {
            const dropdown = document.getElementById('illnessYearDropdown');
            const availableYears = Object.keys(illnessData[Object.keys(illnessData)[0]]).map(Number);

            // Populate the dropdown
            availableYears.forEach(year => {
                const option = document.createElement('option');
                option.value = year;
                option.textContent = year;
                dropdown.appendChild(option);
            });

            // Set default value
            dropdown.value = currentYear;

            // Update the chart when a new year is selected
            dropdown.onchange = function () {
                currentYear = parseInt(this.value, 10);
                monthlyIllnessChart.data.datasets = getDatasetsForYear(currentYear, illnessData);
                monthlyIllnessChart.update();
            };
        };

        setupIllnessYearDropdown();

        // Set an interval to refresh the data every few seconds
        setInterval(() => {
            fetch('/monthly_illness_distribution/')
                .then(response => response.json())
                .then(data => {
                    illnessData = data; // Assign the fetched data to the global variable
                    monthlyIllnessChart.data.datasets = getDatasetsForYear(currentYear, illnessData); // Update the datasets
                    monthlyIllnessChart.update(); // Trigger chart update without animation
                })
                .catch(error => console.error('Error fetching updated data:', error));
        }, 2000); // Update every 2 seconds
    })
    .catch(error => console.error('Error fetching monthly illness distribution data:', error));