const buttons = document.querySelectorAll('.button-container button');

function handleClick(event) {
    buttons.forEach(button => {
        if (button === event.target) {
            button.classList.add('dark');
        } else {
            button.classList.remove('dark');
        }
    });
}

buttons.forEach(button => {
    button.addEventListener('click', handleClick);
});

var date = new Date();
var formattedDate = date.toISOString().split('T')[0];

// Update the content of the present date element
document.getElementById('present-date').textContent = "Date: " + formattedDate;


window.addEventListener('DOMContentLoaded', function() {
    const newsContainer = document.querySelector(".background-image");
    const newsList = newsContainer.querySelector(".news-container");
  
    function removeLastNewsItemIfNeeded() {
      const containerHeight = newsContainer.offsetHeight;
      const contentHeight = newsList.offsetHeight;
  
      if (contentHeight > containerHeight) {
        const newsItems = newsList.getElementsByTagName("li");
        const lastNewsItem = newsItems[newsItems.length - 1];
        if (lastNewsItem) {
          lastNewsItem.remove();
          removeLastNewsItemIfNeeded(); // Check again in case there's still overflow after removal
        }
      }
    }
  
    removeLastNewsItemIfNeeded(); // Check on page load
  });
  
   // Add animation effect to elements with "animation" class
   const animatedElements = document.querySelectorAll('.animation');
   animatedElements.forEach(element => {
       element.style.animation = 'slideIn 1s ease-in-out';
       element.style.animationFillMode = 'forwards';
   });