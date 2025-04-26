let offset = 0;

const slider = document.querySelector(".slider-liner");

document.querySelector(".next").addEventListener("click", next_position)

function next_position(){

    offset = offset+700;

    if(offset > 1400)
    {
        offset = 0;
    }
    slider.style.left =  - offset+ "px"
}

document.querySelector(".prev").addEventListener("click", prev_position);

function prev_position()
{
    offset = offset-700;

    if(offset < 0)
    {
        offset = 1400;
    }
    slider.style.left =  - offset+ "px"

}