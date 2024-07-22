

    let Button  = document.getElementById("submit");
    let InputOne = document.getElementById("inOne");
    let InputTwo = document.getElementById("inTwo");
    let Opt = document.getElementById("options");
    let Result = document.getElementById("result");

    Button.addEventListener('click', function(){
        switch(Opt.value){
            case 'None':
                alert('Please select an option');
                break;
            case 'Add':
                Result.innerHTML = parseInt(InputOne.value) + parseInt(InputTwo.value);
                break;
            case 'Subtract':
                Result.innerHTML = parseInt(InputOne.value) - parseInt(InputTwo.value);
                break;
            case 'Multiply':
                Result.innerHTML = parseInt(InputOne.value) * parseInt(InputTwo.value);
                break;
            case 'Divide':
                Result.innerHTML = parseInt(InputOne.value) / parseInt(InputTwo.value);
                break;
            default:
                alert('Please select an option');
                break;  
        }
    });



