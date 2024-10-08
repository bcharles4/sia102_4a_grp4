document.getElementById('hide').addEventListener('click', function() {
    const button = document.querySelector('.menu button');
    const spanText = button.querySelector('span');

    if (button.id === 'hide') {
      
        button.id = 'menu';
        spanText.innerHTML = "M<br>E<br>N<br>U";

        
        const tl = gsap.timeline();
        tl.to([".sidebar", "#menu"],{
            x: -300,
            duration: 0.5,
            opacity: 1,
            onComplete: function() {
                document.querySelector(".sidebar").style.display = "none";
            }
        });
        
        
        tl.to("#menu", {
            x: 0,
            duration: 0.5,
            opacity: 1,
        });

       

    } else {
      
        button.id = 'hide';
        spanText.innerHTML = "H<br>I<br>D<br>E";

        
        document.querySelector(".sidebar").style.display = "block";
        const tl = gsap.timeline();
        tl.from(".sidebar", {
            x: -500,
            duration: 0.2,
            opacity: 0
        });

        tl.to([".sidebar"], {
            x: 0,
            duration: 0.3,
            opacity: 1
        });

        tl.from("#hide", {
            x: -0,
            duration: .3,
            opacity: 0
        });


        tl.from([".page"], {
            x: -300,
            duration: 0.1,
            opacity: 0
        });

       
    }
});

// Function to set the styles for the clicked page
function setActivePage(page) {
    // Remove the background and font color from all pages
    document.querySelectorAll(".page").forEach(p => {
        p.style.backgroundColor = 'white'; // Reset background color to default
        p.style.color = 'black'; // Reset font color to default
    });

    // Add background and font color to the clicked page
    page.style.backgroundColor = '#333'; // Set background color to dark gray
    page.style.color = 'white'; // Set font color to white
}

// Select all .page elements
const pages = document.querySelectorAll(".page");

// Set the first page as active by default
// if (pages.length > 0) {
//     setActivePage(pages[0]);
// }

// Add click event listeners to all .page elements
pages.forEach(page => {
    page.addEventListener("click", function() {
        setActivePage(page);
    });
});



document.addEventListener("DOMContentLoaded", () => {

const dashB = document.getElementById("dashB");

const tl = gsap.timeline();



tl.from("#dashB",{
    x: -1700,
    duration: .8,
    opacity: 0
});

});

document.addEventListener("DOMContentLoaded", () => {
    const tl = gsap.timeline();
    
    tl.from(".dbE-top",{
        x: 1700,
        duration: 1,
        opacity: 0
    });
});

document.addEventListener("DOMContentLoaded", () => {
    const tl = gsap.timeline();

    tl.from(".dbE-top-right",{
        y: -1700,
        duration: 1,
        opacity: 0
    }) 
});

document.addEventListener("DOMContentLoaded", () => {
    const tl = gsap.timeline();

    tl.from(".dbE-bot-right",{
        x: 1700,
        duration: 1,
        opacity: 0
    }) 
});

document.addEventListener("DOMContentLoaded", () => {
    const tl = gsap.timeline();

    tl.from(".dbE-bot",{
        y: 1700,
        duration: 1,
        opacity: 0
    }) 
});

document.addEventListener("DOMContentLoaded", () => {
    const tl = gsap.timeline();

    tl.from([".main-content"],{
        y: -1500,
        duration: 1,
        opacity: 0
    }) 

    tl.from([".dischargeSummary-main"],{
        x: 1000,
        duration: 0.5,
        opacity: 0
    }) 
});

document.addEventListener("DOMContentLoaded", ()=> {
    const tl = gsap.timeline();
    tl.from(".content",{
        y: 1000,
        duration: 1,
        opacity: 0
    }) 
})


document.querySelectorAll('.page-con').forEach(function(page) {
    page.addEventListener('click', function() {
        // Get the data-url attributes for the pages
        const dashboard = page.getAttribute('data-url-dashboard');
        const patientListUrl = page.getAttribute('data-url-patientList');
        const roomStatusUrl = page.getAttribute('data-url-roomStatus');
        const dischargeRecordsUrl = page.getAttribute('data-url-dischargeRecords');

        // Redirect based on the attribute that exists
        if (dashboard) {
            window.location.href = dashboard;
        } else if (patientListUrl) {
            window.location.href = patientListUrl;
        } else if (roomStatusUrl) {
            window.location.href = roomStatusUrl;
        } else if (dischargeRecordsUrl) {
            window.location.href = dischargeRecordsUrl;
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    const logoutBtn = document.getElementById('logout-btn');
    if (logoutBtn) {
        logoutBtn.addEventListener('click', function() {
            const logoutUrl = logoutBtn.getAttribute('data-url-logout');
            if (logoutUrl) {
                window.location.href = logoutUrl;
            }
        });
    }
});

