class Boss {
    constructor(name, ubicacion, region, descripcion, hp, image, suelta) {
        this.name = name;
        this.ubicacion = ubicacion;
        this.region = region;
        this.descripcion = descripcion;
        this.hp = hp;
        this.image = image;
        this.suelta = suelta;
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const refreshBtn = document.getElementById("refresh-btn");
    const searchInput = document.getElementById("search-input");
    const bossesList = document.getElementById("bosses-list");
    const dlcBtn = document.getElementById("dlc");
    const verApiBtn = document.getElementById("ver-api");
    const overlay = document.createElement("div");
    const expandedCard = document.createElement("div");
    overlay.id = "overlay";
    expandedCard.id = "expanded-card";
    document.body.appendChild(overlay);
    document.body.appendChild(expandedCard);

    const ctx = document.getElementById("bosses-chart").getContext("2d");
    let allBosses = []; // Para almacenar todos los datos de los jefes

    // Obtener datos de la API Flask
    const fetchBossData = async () => {
        try {
            const response = await fetch("http://127.0.0.1:5000/dlc/api"); // Ajusta la URL según sea necesario
            if (!response.ok) {
                throw new Error(`Error al obtener los datos: ${response.statusText}`);
            }
            const data = await response.json();
            allBosses = data.map(
                boss =>
                    new Boss(
                        boss.name,
                        boss.ubicacion,
                        boss.region,
                        boss.descripcion,
                        boss.hp,
                        boss.image,
                        boss.suelta
                    )
            );
            displayBosses(allBosses);
            renderChart(allBosses); // Renderiza el gráfico al inicializar
        } catch (error) {
            console.error("Error al cargar los datos de los jefes:", error);
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

    // Función para expandir la tarjeta
    const expandBossCard = boss => {
        expandedCard.innerHTML = `
            <img src="${boss.image}" alt="${boss.name}" 
                 onerror="this.src='https://via.placeholder.com/300?text=Imagen+No+Disponible';"
                 style="width: 100%; max-width: 300px;">
            <h3>${boss.name}</h3>
            <p><strong>Ubicación:</strong> ${boss.ubicacion || "Desconocida"}</p>
            <p><strong>Región:</strong> ${boss.region || "Desconocida"}</p>
            <p><strong>Salud:</strong> ${boss.hp || "N/A"}</p>
            <p><strong>Descripción:</strong> ${boss.descripcion || "Sin descripción disponible."}</p>
            <p><strong>Suelta:</strong> ${boss.suelta ? boss.suelta.join(', ') : "N/A"}</p>
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
            const ubicacion = boss.ubicacion || "Desconocida";
            acc[ubicacion] = (acc[ubicacion] || 0) + 1;
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

    // Función para buscar jefes
    const searchBosses = () => {
        const query = searchInput.value.toLowerCase();
        const filteredBosses = allBosses.filter(boss =>
            boss.name.toLowerCase().includes(query)
        );
        displayBosses(filteredBosses);
    };

    // Redirigir a la ruta '/'
    const redirectToHome = () => {
        window.location.href = "/";
    };

    const redirectToApi = () => {
        window.location.href = "/dlc/api";
    };

    // Eventos de botones
    verApiBtn.addEventListener("click", redirectToApi);
    refreshBtn.addEventListener("click", fetchBossData);
    searchInput.addEventListener("input", searchBosses);
    dlcBtn.addEventListener("click", redirectToHome);

    // Inicializar datos al cargar la página
    fetchBossData();
});

