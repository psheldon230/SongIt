$(document).ready(function () {
  $("#returnDataPython").click(function () {
    const selectEl = document.getElementById("selectSongs");
    console.log(selectEl);
    const selectedValues = [];
    for (let i = 0; i < selectEl.options.length; i++) {
      if (selectEl.options[i].selected) {
        selectedValues.push(selectEl.options[i].value);
      }
    }
    console.log(selectedValues);
    var responce = sendDataToServer(selectedValues);
    $("#promptText").text("Loading Please Wait");
  });

  $("#selectSongs").change(function () {
    // your code here
    const selectEl = document.getElementById("selectSongs");
    const selectedValues = [];
    for (let i = 0; i < selectEl.options.length; i++) {
      if (selectEl.options[i].selected) {
        selectedValues.push(selectEl.options[i].value);
      }
    }
    sendSelectedAlbumsToServer(selectedValues);
  });

  function setupGraph() {
    const data = [
      { x: 10, y: 20 },
      { x: 20, y: 40 },
      { x: 30, y: 60 },
      { x: 40, y: 80 },
      { x: 50, y: 100 },
    ];

    const margin = { top: 20, right: 20, bottom: 50, left: 50 };
    const width = 500 - margin.left - margin.right;
    const height = 500 - margin.top - margin.bottom;

    const svg = d3
      .select("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom);

    const xScale = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.x)])
      .range([margin.left, width - margin.right]);

    const yScale = d3
      .scaleLinear()
      .domain([0, d3.max(data, (d) => d.y)])
      .range([height - margin.bottom, margin.top]);

    const xAxis = d3.axisBottom(xScale);

    const yAxis = d3.axisLeft(yScale);

    svg
      .append("g")
      .attr("transform", `translate(0, ${height - margin.bottom})`)
      .call(xAxis);

    svg
      .append("g")
      .attr("transform", `translate(${margin.left}, 0)`)
      .call(yAxis);

    svg
      .selectAll(".dot")
      .data(data)
      .enter()
      .append("circle")
      .attr("class", "dot")
      .attr("cx", (d) => xScale(d.x))
      .attr("cy", (d) => yScale(d.y))
      .attr("r", 5)
      .style("fill", "steelblue");
  }
  // setupGraph();

});
function formatTextForHTML(text) {
  // Replace newline characters with HTML line breaks
  // const formattedText = text.replace(/\n/g, "<br>");
  // const formattedText = text
  var formattedText = text;
  return formattedText;


  // Replace consecutive whitespace characters with non-breaking spaces
  return formattedText.replace(/[\s]+/g, "&nbsp;");
}

function sendSelectedAlbumsToServer(data) {
  $.ajax({
    url: "/process-album-cover-data",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      // console.log(response.message);
      console.log(response);
      imageUrls = response.message;
      const boxes = document.querySelectorAll(".containerBottom .box");
      boxes.forEach((box, index) => {
        box.style.backgroundImage = `url(${imageUrls[index]})`;
      });
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      $("#promptText").text("Error sending data");
      console.log(textStatus);
    },
  });
}


function sendDataToServer(data) {
  $.ajax({
    url: "/process-data",
    method: "POST",
    data: JSON.stringify(data),
    contentType: "application/json",
    success: function (response) {
      console.log("Data sent successfully");
      console.log(response.message);


      $("#promptText").text(response.message);
    },
    error: function (jqXHR, textStatus, errorThrown) {
      console.log("Error sending data");
      $("#promptText").text("Error sending data");

      console.log(textStatus);
    },
  });
}
