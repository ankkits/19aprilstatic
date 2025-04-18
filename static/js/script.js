document.querySelector(".icon-menu").addEventListener("click", function (event) {
  event.preventDefault();
  document.body.classList.toggle("menu-open");
});

const spollerButtons = document.querySelectorAll("[data-spoller] .spollers-faq__button");

spollerButtons.forEach((button) => {
  button.addEventListener("click", function () {
    const currentItem = button.closest("[data-spoller]");
    const content = currentItem.querySelector(".spollers-faq__text");

    const parent = currentItem.parentNode;
    const isOneSpoller = parent.hasAttribute("data-one-spoller");

    if (isOneSpoller) {
      const allItems = parent.querySelectorAll("[data-spoller]");
      allItems.forEach((item) => {
        if (item !== currentItem) {
          const otherContent = item.querySelector(".spollers-faq__text");
          item.classList.remove("active");
          otherContent.style.maxHeight = null;
        }
      });
    }

    if (currentItem.classList.contains("active")) {
      currentItem.classList.remove("active");
      content.style.maxHeight = null;
    } else {
      currentItem.classList.add("active");
      content.style.maxHeight = content.scrollHeight + "px";
    }
  });
});

// Form submission handler
//function handleSubmit(event) {
//  event.preventDefault();
  
  // Get form data
 // const formData = {
 //   name: document.getElementById('name').value,
 //   phone: document.getElementById('phone').value,
 //   email: document.getElementById('email').value,
  //  message: document.getElementById('message').value
 // };

  // TODO: Replace this with your actual Python function call
  // This is a placeholder for the Python function that will handle the form submission
 // console.log('Form submitted with data:', formData);
  
  // Example of how to call a Python function (to be implemented)
  /*
  fetch('/submit_form', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify(formData)
  })
  .then(response => response.json())
  .then(data => {
    console.log('Success:', data);
    // Show success message to user
  })
  .catch((error) => {
    console.error('Error:', error);
    // Show error message to user
  });
  */

  return false;
}
