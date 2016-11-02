function draw(data) {
	console.log(data);

	var tr = d3.select('#data').selectAll('table')
    .data(data.serie)
    .enter()
    .append('tr');

    tr.append('td')
    .text(function(d) {
      return d.nom;
    });

    tr.append('td')
    .append('div')
    .style('width', function(d) {
      return (d.nombreVotes) + 'px';
    })
    .style('background-color','#168ccc')
    .style('height','10px');
}

d3.json("../test.json", draw);