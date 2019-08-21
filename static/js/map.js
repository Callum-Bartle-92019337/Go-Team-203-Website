// Gets the ID of the elements we are changing ================================
const LIGHTS_BUTTON_ID = document.getElementById( 'lights' );
const BACKGROUND_1_ID = document.querySelector( '.about' );
const BACKGROUND_2_ID = document.querySelector( 'html' );

// Defines the functions ======================================================
// Map stuff
function initMap() {
  var options = {
    zoom: 15,
    center: {
      lat: -43.532055,
      lng: 172.636230
    }
  };
  var map = new google.maps.Map( document.getElementById( 'mapp' ), options );
}

// Gets the background color of an element
var myFunction = function() {
  console.log( "Testing" )
}();

function getBGColor( element ) {
  return element.style.backgroundColor;
}

// Sets the background color of an element
function setBGColor( element, color ) {
  element.style.backgroundColor = color;
}

// Change the colors between black and default
function lightsToggle() {
  if ( getBGColor( BACKGROUND_1_ID ) == 'rgb(31, 40, 159)' ) {
    setBGColor( BACKGROUND_1_ID, 'rgb(0, 0, 0)' );
    setBGColor( BACKGROUND_2_ID, 'rgb(0, 0, 0)' );
  } else {
    setBGColor( BACKGROUND_1_ID, 'rgb(31, 40, 159)' );
    setBGColor( BACKGROUND_2_ID, 'rgb(182, 224, 255)' );
  }
}

// Starts the script ==========================================================
// Starting color
setBGColor( BACKGROUND_1_ID, 'rgb(31, 40, 159)' );

// If the button exists continue
if ( LIGHTS_BUTTON_ID ) {
  // Adds some atributes to the empty element
  LIGHTS_BUTTON_ID.setAttribute( "class", 'btn' );
  LIGHTS_BUTTON_ID.setAttribute( "title", 'Lights' );
  LIGHTS_BUTTON_ID.setAttribute( "href", '#' );
  LIGHTS_BUTTON_ID.textContent = "Lights";

  // Binds the event
  LIGHTS_BUTTON_ID.addEventListener( "click", function( e ) {
    e.preventDefault();
    lightsToggle();
  } );
};
