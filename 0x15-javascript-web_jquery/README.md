# Web jQuery

# Learning Objectives

- How to select HTML elements with jQuery
- What are differences between `ID`, `class` and `tag name` selectors
- How to modify an HTML element style
- How to get and update an HTML element content
- How to modify the DOM
- How to make a `GET` request with jQuery Ajax
- How to make a `POST` request with jQuery Ajax
- How to listen/bind to DOM events
- How to listen/bind to user events

# Tasks

## No jQuery

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`):

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Write a Javascript script that updates the text color of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Write a Javascript script that adds the class `red` to the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#red_header`:

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Write a Javascript script that toggles the class of the HTML tag `HEADER` to red (`#FF0000`) when the user clicks on the tag `DIV#toggle_header`:

- The `HEADER` tag must always have one class: `red` or `green`, never both in the same time, never empty.
- If the current class is `red`, when the user click on `DIV#toggle_header`, the class must be updated to `green`; and the reverse.
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

P
Write a Javascript script that adds a `LI` element to a list when the user clicks on the tag `DIV#add_item`:

- The new element must be: `<li>Item</li>`
- The new element must be added to `UL.my_list`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

## Change the text

Write a Javascript script that updates the text of the HTML tag `HEADER` to “New Header!!!” when the user clicks on `DIV#update_header`

- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

`

Write a Javascript script that fetches and replaces the `name` of this URL: `https://swapi-api.hbtn.io/api/people/5/?format=json`

- The name must be displayed in the HTML tag `DIV#character`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

Write a Javascript script that fetches and lists all movies title by using this URL: `https://swapi-api.hbtn.io/api/films/?format=json`

- All movie titles must be list in the HTML tag `UL#list_movies`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API

## Say Hello!

Write a Javascript script that fetches from `https://fourtonfish.com/hellosalut/?lang=fr` and displays the value of `hello` from that fetch in the HTML’s tag `DIV#hello`.

- The translation of “hello” must be display in the HTML tag `DIV#hello`
- You can’t use `document.querySelector` to select the HTML tag
- You must use the jQuery API
- Your script must work when it is imported from the `HEAD` tag
