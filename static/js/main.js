function mostrarGrafico(grafico) {
    const graficoContainer = document.getElementById("graficoContainer");

    let titulo = "";
    let descricao = "";
    let imagemSrc = "";

    switch (grafico) {
        case "grafico1":
            titulo = "Gráfico de Consumo de Álcool por Faixa Etária";
            descricao =
                "Esse gráfico permite visualizar como o consumo de álcool varia entre diferentes faixas etárias, ajudando a identificar tendências e padrões de comportamento entre as idades.";
            imagemSrc = "../static/imgs/consumo-alcool-idade.png";
            break;
        case "grafico2":
            titulo = "Relação entre a pressão sistólica e diastólica por Status de bebedor";
            descricao = "Este gráfico permite analisar como o consumo de álcool influencia os níveis de pressão arterial sistólica e diastólica.";
            imagemSrc = "../static/imgs/scatterplot-sistolica-diastolica-bebedor.png";
            break;
        case "grafico3":
            titulo = "Heatmap";
            descricao =
                "O heatmap permite visualizar as correlações entre as variáveis da base de dados, destacando relações mais fortes ou fracas entre elas.";
            imagemSrc = "../static/imgs/heatmap_por_consumo.png";
            break;
        case "grafico4":
            titulo = "Gráfico de Triglicerídeos por Consumo de Álcool";
            descricao = "Este gráfico permite observar como os níveis de triglicerídeo variam em relação ao consumo de álcool.";
            imagemSrc = "../static/imgs/triglicerideos_por_consumo.png";
            break;
        case "grafico5":
            titulo = "Relação entre Glicose e Colesterol Total por Consumo de Álcool";
            descricao = "Este gráfico permite observar a relação entre os níveis de glicose e colesterol total com o consumo de álcool.";
            imagemSrc = "../static/imgs/scatterplot_glicose_colesterol.png";
            break;
        case "grafico6":
            titulo = "Gráfico de Barras Empilhadas para ver o consumo de Álcool por Faixa de Peso";
            descricao =
                "Esse gráfico permite observar como o peso se distribui entre aqueles que consomem e não consomem bebidas. Se uma faixa de peso tiver uma proporção significativamente maior de consumidores ou não consumidores, isso pode sugerir um padrão interessante sobre a relação entre peso e consumo de álcool.";
            imagemSrc = "../static/imgs/consumo-alcool-peso.png";
            break;
        case "grafico7":
            titulo = "Gráfico de Barras para ver a relação de fumantes e o consumo de álcool";
            descricao =
                "Neste gráfico, você verá as barras empilhadas que mostram o número de pessoas em cada categoria de consumo de álcool (bebedores e não bebedores), dentro de cada status de fumante (não fumante, ex-fumante e fumante). Isso oferece uma visão clara das proporções de cada grupo e como o consumo de álcool se relaciona ao status de fumante.";
            imagemSrc = "../static/imgs/relacao_fumante_e_bebedor.png";
            break;
    }

    // Atualiza o conteúdo do container com o gráfico e informações correspondentes
    graficoContainer.innerHTML = `
        <h3>${titulo}</h3>
        <img src="${imagemSrc}" alt="${titulo}">
        <p>${descricao}</p>
    `;
}
