//Default data
function buildPlots() {
    const defaultUrl = "/sample/BB_940";
    console.log(defaultUrl);
    d3.json(defaultUrl).then(function(data){
        let pie_data = [data[0].pie_data[0]];
        let bubble_data = [data[0].bubble_data[0]];
        let meta_data = [data[0].metaData];

        console.log(data);
        //Plots
        Plotly.newPlot("pie", pie_data);
        Plotly.newPlot("bubble", bubble_data);

        //Metadata

    });
};


//Update datasets
function update(sample) {
    let url = `/sample/BB_${sample}`;
    console.log(`New URL: ${url}`);
    d3.json(url).then(function(data){
        let pie_data = [data[0].pie_data[0]];
        let bubble_data = [data[0].bubble_data[0]];
        let meta_data = [data[0].metaData];

        console.log(data);
        updatePlots(pie_data, bubble_data, meta_data);
    }).catch(console.error);
};

//Update plots
function updatePlots(pie_data, bubble_data, meta_data) {
    //Restyle Pie
    Plotly.restyle("pie", "values", [pie_data.values]);
    Plotly.restyle("pie", "labels", [pie_data.labels]);
    Plotly.restyle("pie", "hoverinfo", [pie_data.hoverinfo]);

    //Restyle Bubble
    Plotly.restyle("bubble", "x", [bubble_data.x]);
    Plotly.restyle("bubble", "y", [bubble_data.y]);
    Plotly.restyle("bubble", "marker", [bubble_data.marker]);
    Plotly.restyle("bubble", "text", [bubble_data.text]);

    //Update Meta
};

buildPlots();