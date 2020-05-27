function DraWChat()
{
 max = {{max}}
 
    var barData = {
                   labels : [
                          {% for item in labels %}
                           "{{ item }}",
                          {% endfor %}
                          ],

                  datasets : [{
                      backgroundColor: "{{color}}",
                      label: "Cases:",
                      data :  [
                                {% for item in values %}
                                   "{{ item }}",
                                  {% endfor %}
                                ]
                        }],
                }
    
      var option = {
                scales: {
                  yAxes: [
                    {
                      stacked: true,
                      gridLines: {
                        display: true,
                        color: "{{color}}"
                      },
                      ticks: {
                        suggestedMax: max,
                        suggestedMin: 0
                      }
                    }
                  ],
                  xAxes: [
                    {
                      gridLines: {
                        display: false
                      }
                    }
                  ]
                }
              };

     //get bar chart canvas
     var mychart = document.getElementById("chart").getContext("2d");
     // draw bar chart
     var myBarChart = new Chart(mychart, {
                                  type: 'bar',
                                  data: barData,
                                  options: option
                              });
     
     
}
  