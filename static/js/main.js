class Boss {
    constructor(name, location, region, description, health, image, drops) {
        this.name = name;
        this.location = location;
        this.region = region;
        this.description = description;
        this.health = health;
        this.image = image;
        this.drops = drops;
    }
}

const API_URL = "https://eldenring.fanapis.com/api/bosses?limit=300";

document.addEventListener("DOMContentLoaded", () => {
    const refreshBtn = document.getElementById("refresh-btn");
    const searchInput = document.getElementById("search-input");
    const bossesList = document.getElementById("bosses-list");
    const verApiBtn = document.getElementById("ver-api");
    const overlay = document.createElement("div");
    const expandedCard = document.createElement("div");
    overlay.id = "overlay";
    expandedCard.id = "expanded-card";
    document.body.appendChild(overlay);
    document.body.appendChild(expandedCard);

    const ctx = document.getElementById("bosses-chart").getContext("2d");
    let allBosses = []; // Para almacenar todos los datos de los jefes

    // Función para obtener y mostrar los datos
    const fetchBosses = async () => {
        try {
            const response = await fetch(API_URL);
            const data = await response.json();
            allBosses = data.data.map(
                boss => new Boss(
                    boss.name, 
                    boss.location, 
                    boss.region, 
                    boss.description, 
                    boss.healthPoints, 
                    boss.image, 
                    boss.drops
                )
            );
            displayBosses(allBosses);
            renderChart(allBosses); // Llamamos a la función para renderizar el gráfico
        } catch (error) {
            console.error("Error fetching data:", error);
        }
    };

    // Función para mostrar las tarjetas
    const displayBosses = bosses => {
        bossesList.innerHTML = ""; // Limpia la lista
        bosses.forEach(boss => {
            const bossCard = document.createElement("div");
            bossCard.classList.add("boss-card");
            bossCard.innerHTML = `
                <div class="boss-image">
                    <img src="${boss.image}" alt="${boss.name}" 
                         onerror="this.src='https://via.placeholder.com/150?text=Sin+Imagen';"
                         style="width: 100%; max-width: 80px; height: auto; border-radius: 50%;">
                </div>
                <div class="boss-info">
                    <h3>${boss.name}</h3>
                </div>
            `;
            bossCard.addEventListener("click", () => expandBossCard(boss));
            bossesList.appendChild(bossCard);
        });
    };

    // Filtrar jefes por nombre
    const filterBosses = query => {
        const filteredBosses = allBosses.filter(boss =>
            boss.name.toLowerCase().includes(query.toLowerCase())
        );
        displayBosses(filteredBosses);
    };

    // Expande la tarjeta para mostrar más información
    const expandBossCard = boss => {
        expandedCard.innerHTML = `
            <img src="${boss.image}" alt="${boss.name}" 
                 onerror="this.src='https://via.placeholder.com/300?text=Imagen+No+Disponible';"
                 style="width: 100%; max-width: 300px;">
            <h3>${boss.name}</h3>
            <p><strong>Ubicación:</strong> ${boss.location || "Desconocida"}</p>
            <p><strong>Región:</strong> ${boss.region || "Desconocida"}</p>
            <p><strong>Salud:</strong> ${boss.health || "N/A"}</p>
            <p><strong>Descripción:</strong> ${boss.description || "Sin descripción disponible."}</p>
            <p><strong>Suelta:</strong> ${boss.drops ? boss.drops.join(', ') : "N/A"}</p>
            <button id="close-expanded">Cerrar</button>
        `;
        overlay.style.display = "block";
        expandedCard.style.display = "block";

        document.getElementById("close-expanded").addEventListener("click", closeExpandedCard);
    };

    // Cierra la tarjeta ampliada
    const closeExpandedCard = () => {
        overlay.style.display = "none";
        expandedCard.style.display = "none";
    };

    // Función para renderizar el gráfico por ubicación
    const renderChart = bosses => {
        const ctx = document.getElementById("bosses-chart").getContext("2d");
        const bossLocations = bosses.reduce((acc, boss) => {
            const location = boss.location || "Desconocida";
            acc[location] = (acc[location] || 0) + 1;
            return acc;
        }, {});
    
        const chartData = {
            labels: Object.keys(bossLocations), // Ubicaciones se usan como etiquetas
            datasets: [
                {
                    label: "Cantidad de Jefes por Ubicación",
                    data: Object.values(bossLocations),
                    backgroundColor: [
                        "#e06c75", "#98c379", "#61afef", "#c678dd", "#e5c07b"
                    ],
                },
            ],
        };
    
        new Chart(ctx, {
            type: "bar",  // Cambié a gráfico de barras para una mejor visualización
            data: chartData,
            options: {
                responsive: true,
                scales: {
                    x: {
                        ticks: {
                            display: false,  // Oculta las etiquetas del eje X
                        },
                    },
                    y: {
                        beginAtZero: true,
                    },
                },
                plugins: {
                    tooltip: {
                        callbacks: {
                            label: function(tooltipItem) {
                                // Muestra el nombre de la ubicación y la cantidad al pasar el ratón
                                const location = tooltipItem.label;
                                const count = tooltipItem.raw;
                                return `${location}: ${count} Jefes`;
                            },
                        },
                    },
                },
            },
        });
    };
    

    // Event Listeners
    refreshBtn.addEventListener("click", fetchBosses);
    searchInput.addEventListener("input", e => filterBosses(e.target.value));
    dlc.addEventListener("click", function() {
        window.location.href = '/dlc';  // Aquí colocas la ruta hacia la nueva página
    });
    verApiBtn.addEventListener("click", function() {
        window.location.href = 'https://eldenring.fanapis.com/api/bosses?limit=300';  // Aquí colocas la ruta hacia la nueva página
    });
    // Cierra el overlay al hacer clic
    overlay.addEventListener("click", closeExpandedCard);

    // Inicializa la página
    fetchBosses();
});
