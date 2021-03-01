function error(err) {
console.log("using SFU as default")
    map([-122.9180,49.2768])
}

function success(position) {
    const latitude  = position.coords.latitude;
    const longitude = position.coords.longitude;
    map([longitude,latitude])
}

navigator.geolocation.getCurrentPosition(success,error)
  /* Toggle the sidebar */

  let toggleStatus = false;

        function toggleNav(){
          if (toggleStatus === false){
            toggleStatus = true;
            var x = window.matchMedia("(max-width: 1820px)");
            var x1 = window.matchMedia("(min-width: 1520px)");
            var y = window.matchMedia("(max-width: 1520px)");
            var y1 = window.matchMedia("(min-width: 1300px)");
            var z = window.matchMedia("(max-width: 1300px)");
            var z1 = window.matchMedia("(min-width: 1024px)");
            var a = window.matchMedia("(max-width: 1024px)");
            var a1= window.matchMedia("(min-width: 900px)");
            var b = window.matchMedia("(max-width: 900px)");
            var b1= window.matchMedia("(min-width: 768px)");
            var c = window.matchMedia("(max-width: 768px)");
            var c1= window.matchMedia("(min-width: 600px)");
            var d = window.matchMedia("(max-width: 600px)");
            var d1= window.matchMedia("(min-width: 100px)");

            // 1520px - 1820px
            if (x.matches && x1.matches) {
              document.getElementById("sidebar").style.width = "30vw";
              document.getElementById("table-container").style.width = "30vw";
            }

            //1300px - 1520px
            else if (y.matches && y1.matches) {
              document.getElementById("sidebar").style.width = "35vw";
              document.getElementById("table-container").style.width = "35vw";
            }
            //1024px - 1300px
            else if (z.matches && z1.matches) {
              document.getElementById("sidebar").style.width = "50vw";
              document.getElementById("table-container").style.width = "50vw";
              document.getElementById("table-container").style.height = "70vh";
            }
            //900 px-1024px
            else if (a.matches && a1.matches) {
              document.getElementById("sidebar").style.width = "60vw";
              document.getElementById("table-container").style.width = "60vw";
            }
            //768px - 900px
            else if (b.matches && b1.matches) {
              document.getElementById("sidebar").style.width = "70vw";
              document.getElementById("table-container").style.width = "70vw";
              document.getElementById("table-container").style.height = "65vh";
            }
            //600px - 768px
            else if (c.matches && c1.matches) {
              document.getElementById("sidebar").style.width = "80vw";
              document.getElementById("table-container").style.width = "80vw";
            }
            //100px - 600px
            else if (d.matches && d1.matches) {
              document.getElementById("sidebar").style.width = "100vw";
              document.getElementById("table-container").style.width = "100vw";
              document.getElementById("table-container").style.height = "45vh";
            }
            else {
              document.getElementById("sidebar").style.width = "25vw";
              document.getElementById("table-container").style.width = "25vw";
            }

          }

          else if (toggleStatus === true){
            document.getElementById("sidebar").style.width = "0vw";
            document.getElementById("table-container").style.width = "0vw";
            toggleStatus = false;
          }
        }




/* Flip the arrow icon on the side */
$(document).ready(function() {
    $( ".toggle" ).click( function() {
        $("#open_sidebar").toggleClass('flip')
    });
    });
