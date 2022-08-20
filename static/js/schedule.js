const queryString = window.location.search;
const urlParams = new URLSearchParams(queryString);
week = urlParams.get("week");

if(week != null){
    document.getElementById(week).scrollIntoView({block: 'center',})
}
