// javascript

// const dataBridge = document.getElementById('data-bridge');
// const serverData = JSON.parse(dataBridge.dataset.serverInfo);
// console.log(serverData);

async function fetchData() {
    url = 'http://localhost:80/data'
    try {
        const response = await fetch(url);
        
        if (!response.ok) {
            throw new Error(`HTTP error! Status: ${response.status}`);
        }
        
        // This parses the JSON string back into a JavaScript object
        const data = await response.json(); 
        
        console.log(data);
        console.log(data.status); // Outputs: "success"
    } catch (error) {
        console.error("Failed to fetch data:", error);
    }
}

fetchData()

// d3.select()
// d3.selectAll();


d3.select('h1').style('color','red') // Will get first h1 element from DOM
    .attr('class', 'heading') //Can append class or id tag
    .text('Updated h1 tag');  //Can inject text into tag


d3.select('body').append('p').text('First Paragraph');

