//Default data
function buildPlots() {
    const defaultUrl = "/sample/BB_940";
    console.log(defaultUrl);
    d3.json(defaultUrl).then(function(data){
        let pie_data = [data[0].pie_data[0]];
        let bubble_data = [data[0].bubble_data[0]];
        let meta_data = [data[0].metaData];

        console.log(data);

        Plotly.newPlot("pie", pie_data);
        Plotly.newPlot("bubble", bubble_data);
    });
};


//Update Page
function update(sample) {
    let url = `/sample/BB_${sample}`
    d3.json(defaultUrl).then(function(data){
        let pie_data = [data[0].pie_data[0]];
        let bubble_data = [data[0].bubble_data[0]];
        let meta_data = [data[0].metaData];

        console.log(data);

        Plotly.newPlot("pie", pie_data);
        Plotly.newPlot("bubble", bubble_data);
    });
};

buildPlots();