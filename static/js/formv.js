/*
 ** This script validates the content for a form based on specific rules
 ** for each item in the form
 */

// Once the pages is loaded run the init function
window.onload = init;

var valid,
  FIRSTNAME_ERROR,
  FNAME_ERROR,
  EMAIL_ERROR,
  GENDER_ERROR,
  INTERESTS_ERROR,
  REGION_ERROR,
  TOS_ERROR,
  FIRSTNAME_MSG,
  FAMILYNAME_MSG,
  EMAIL_MSG,
  SEX_MSG,
  INTERESTS_MSG,
  REGION_MSG,
  TANDCAGREE_MSG,
  EMAILREGEXP

function init() {
  var formsubmit = document.getElementById( "submit" );

  //Sets valid
  valid = true;

  //Set error messages
  FIRSTNAME_ERROR = "First name should be at least 2 letters in length";
  FNAME_ERROR = "Family name should be at least 2 letters in length";
  EMAIL_ERROR = "Must be a valid email address, or left blank";
  GENDER_ERROR = "Please select one.";
  INTERESTS_ERROR = "Please select at least one source";
  REGION_ERROR = "You must choose a region.";
  TOS_ERROR = "You must agree to the terms and conditions to continue.";

  //Get error field IDs
  FIRSTNAME_MSG = document.getElementById( 'firstname_msg' );
  FAMILYNAME_MSG = document.getElementById( 'familyname_msg' );
  EMAIL_MSG = document.getElementById( 'email_msg' );
  SEX_MSG = document.getElementById( 'sex_msg' );
  INTERESTS_MSG = document.getElementById( 'interests_msg' );
  REGION_MSG = document.getElementById( 'region_msg' );
  TANDCAGREE_MSG = document.getElementById( 'tandcagree_msg' );

  //Store email pattern
  EMAILREGEXP = /^(\w+@[a-z\d]+?([a-z-\d_\.]*?)\.[a-z]{2,6})$/i;

  // Check if the for button exists then bind event
  if ( formsubmit ) {
    formsubmit.onclick = checkForm;
  }
}

// Remove the error from an element
function errorReset( element ) {
  element.innerHTML = "";
  element.className = '';
}

// Adds an error to an element
function errorPass( element, errorMsg ) {
  element.innerHTML = '' + errorMsg + '';
  element.className = 'error';
  valid = false;
}

function checkForm() {

  //Get the form information
  var firstname = document.getElementById( 'firstname' ).value;
  var familyname = document.getElementById( 'familyname' ).value;
  var email = document.getElementById( 'email' ).value;
  var sex_male = document.getElementById( 'sex_male' ).checked;
  var sex_female = document.getElementById( 'sex_female' ).checked;
  var interests = document.contactform[ 'interests[]' ];
  var interestcount = 0;
  var region = document.getElementById( 'region' ).value;
  var tandcagree = document.getElementById( 'tandcagree' ).checked;
  valid = true;

  //First name check
  firstname.length < 2
    ? errorPass( FIRSTNAME_MSG, FIRSTNAME_ERROR )
    : errorReset( FIRSTNAME_MSG );

  //Last name check
  familyname.length < 2
    ? errorPass( FAMILYNAME_MSG, FNAME_ERROR )
    : errorReset( FAMILYNAME_MSG );

  //Email check
  email != "" && !EMAILREGEXP.test( email )
    ? errorPass( EMAIL_MSG, EMAIL_ERROR )
    : errorReset( EMAIL_MSG );

  //Gender
  !sex_male && !sex_female && !sex_other
    ? errorPass( SEX_MSG, GENDER_ERROR )
    : errorReset( SEX_MSG );

  //Interests
  for ( var i = 0; i < interests.length; i++ ) {
    if ( interests[ i ].checked ) {
      interestcount++;
    }
  }
  interestcount < 1
    ? errorPass( INTERESTS_MSG, INTERESTS_ERROR )
    : errorReset( INTERESTS_MSG );

  //Region
  region == -1
    ? errorPass( REGION_MSG, REGION_ERROR )
    : errorReset( REGION_MSG );

  //Terms of service
  !tandcagree
    ? errorPass( TANDCAGREE_MSG, TOS_ERROR )
    : errorReset( TANDCAGREE_MSG );
  return valid;
}
