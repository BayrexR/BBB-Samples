//Default data
function buildPlots() {
    const defaultUrl = "/sample/BB_940";
    console.log(defaultUrl);
    d3.json(defaultUrl).then(function(data){
        let pie_data = [data[0].pie_data[0]];
        let bubble_data = [data[0].bubble_data[0]];
        let meta_data = [data[0].metadata[0]];

        console.log(data);
        //Plots
        Plotly.newPlot("pie", pie_data);
        Plotly.newPlot("bubble", bubble_data);

        //Metadata
        d3.select("#age").text(`Age: ${meta_data[0].AGE}`);
        d3.select("#bb_type").text(`BBTYPE: ${meta_data[0].BBTYPE}`);
        d3.select("#ethnicity").text(`Ethnicity: ${meta_data[0].ETHNICITY}`);
        d3.select("#gender").text(`Gender: ${meta_data[0].GENDER}`);
        d3.select("#location").text(`Location: ${meta_data[0].LOCATION}`);
        d3.select("#sample_id").text(`Sample ID: ${meta_data[0].sample}`);
    });
};


//Update datasets
function update(sample) {
    let url = `/sample/BB_${sample}`;
    console.log(`New URL: ${url}`);
    d3.json(url).then(function(data){
        let pie_data = [data[0].pie_data[0]];
        let bubble_data = [data[0].bubble_data[0]];
        let meta_data = [data[0].metadata[0]];

        console.log(data);
        updatePlots(pie_data, bubble_data, meta_data);
    }).catch(console.error);
};

//Update plots
function updatePlots(pie_data, bubble_data, meta_data) {

    //Restyle Pie
    Plotly.restyle("pie", "values", [pie_data[0].values]);
    Plotly.restyle("pie", "labels", [pie_data[0].labels]);
    Plotly.restyle("pie", "hoverinfo", [pie_data[0].hoverinfo]);

    //Restyle Bubble
    Plotly.restyle("bubble", "x", [bubble_data[0].x]);
    Plotly.restyle("bubble", "y", [bubble_data[0].y]);
    Plotly.restyle("bubble", "marker", [bubble_data[0].marker]);
    Plotly.restyle("bubble", "text", [bubble_data[0].text]);

    //Update Meta
    d3.select("#age").text(`Age: ${meta_data[0].AGE}`);
    d3.select("#bb_type").text(`BBTYPE: ${meta_data[0].BBTYPE}`);
    d3.select("#ethnicity").text(`Ethnicity: ${meta_data[0].ETHNICITY}`);
    d3.select("#gender").text(`Gender: ${meta_data[0].GENDER}`);
    d3.select("#location").text(`Location: ${meta_data[0].LOCATION}`);
    d3.select("#sample_id").text(`Sample ID: ${meta_data[0].sample}`);
};

buildPlots();