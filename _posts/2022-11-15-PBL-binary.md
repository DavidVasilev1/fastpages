---
title: Binary Math
layout: default
description: A Binary Math illustrative application using HTML, Liquid, and JavaScript.
permalink: /binary
categories: [Html, Liquid, Javascript, Tri 2 Assignments, Trimester 2, Markdown]
---

<!-- Hack 1: add a character display to text when 8 bits, determine if printable or not printable -->
<!-- Hack 2: change to 24 bits and add a color code and display color when 24 bits, think about display on this one -->
<!-- Hack 3: do your own thing -->

{% assign BITS = 8 %}
<div class="container bg-primary">
    <header class="pb-3 mb-4 border-bottom border-primary text-dark">
        <h1 style="text-align: center;">Binary Math with Conversions</h1>
    </header>
    <style>
        .table {
            text-align: center;
            margin-left: auto;
            margin-right: auto;
        }
        .row {
            margin-left: auto;
            margin-right: auto;
        }
        .box {
            width: 800px;
        }
    </style>
    <div class="row justify-content-md-center">
        <div class="col-8">
            <table class="table">
            <tr id="table">
                <th>Plus</th>
                <th>Binary</th>
                <th>Octal</th>
                <th>Hexadecimal</th>
                <th>Decimal</th>
                <th>Character</th>
                <th>Bits</th>
                <th>Minus</th>
            </tr>
            <tr>
                <td><button type="button" id="add1" onclick="add(1)">+1</button></td>
                <td id="binary">00000000</td>
                <td id="octal">0</td>
                <td id="hexadecimal">0</td>
                <td id="decimal">0</td>
                <td id="character"></td>
                <td id="bits">{{BITS}}</td>
                <td><button type="button" id="sub1" onclick="add(-1)">-1</button></td>
            </tr>
            </table>
        </div>
        <div class="col-12">
            {% comment %}Liquid for loop includes last number, thus the Minus{% endcomment %}
            {% assign bits = BITS | minus: 1 %} 
            <table class="table">
            <tr>
                {% comment %}Build many bits{% endcomment %}
                {% for i in (0..bits) %}
                <td><img class="img-responsive py-3" id="bulb{{ i }}" src="{{site.baseurl}}/images/off.png" width="60" height="Auto" style="margin-left: auto; margin-right: auto;">
                    <button type="button" id="butt{{ i }}" onclick="javascript:toggleBit({{ i }})">Turn on</button>
                </td>
                {% endfor %}
            </tr>
            <tr>
                {% comment %}Value of bit{% endcomment %}
                {% for i in (0..bits) %}
                <td><input type='text' id="digit{{ i }}" Value="0" size="1" readonly></td>
                {% endfor %}
            </tr>
            </table>
        </div>
    </div>
</div>

<div class="container bg-primary">
    <h1>RGB</h1>
    <header class="pb-3 mb-4 border-bottom border-primary text-dark">
    </header>
    <style>
        .table {
            text-align: center;
            margin-left: auto;
            margin-right: auto;
        }
        .row {
            margin-left: auto;
            margin-right: auto;
        }
    </style>
    <div class="row justify-content-md-center">
        <div class="col-8">
            <table class="table">
            <tr id="table">
                <th>RGB</th>
                <th>Plus</th>
                <th>Binary</th>
                <th>Hexadecimal</th>
                <th>Decimal</th>
                <th>Minus</th>
                <th>Color</th>
            </tr>
            <tr>
                <td>R<input type="range" min="0" max="255" value="0" id="sliderR" style="width: 1px;"></td>
                <td><button type="button" id="addCR" onclick="addR(1)">+1</button></td>
                <td id="binR">00000000</td>
                <td id="hexR">0</td>
                <td id="decR">0
                </td>
                <td><button type="button" id="subCR" onclick="addR(-1)">-1</button></td>
                <td rowspan="3" class="box" id="color"></td>
            </tr>
            <tr>
                <td>G<input type="range" min="0" max="255" value="0" id="sliderG" style="width: 1px;"></td>
                <td><button type="button" id="addCG" onclick="addG(1)">+1</button></td>
                <td id="binG">00000000</td>
                <td id="hexG">0</td>
                <td id="decG">0</td>
                <td><button type="button" id="subCG" onclick="addG(-1)">-1</button></td>
            </tr>
            <tr>
                <td>B<input type="range" min="0" max="255" value="0" id="sliderB" style="width: 1px;"></td>
                <td><button type="button" id="addCB" onclick="addB(1)">+1</button></td>
                <td id="binB">00000000</td>
                <td id="hexB">0</td>
                <td id="decB">0</td>
                <td><button type="button" id="subCB" onclick="addB(-1)">-1</button></td>
            </tr>
            </table>
        </div>
    </div>
        <div class="col-12">
            {% assign bits = BITS | minus: 1 %} 
            <table class="tableR">
            <tr>
                {% comment %}Build many bits{% endcomment %}
                {% for i in (0..bits) %}
                <td><img class="img-responsive py-3" id="bulbR{{ i }}" src="{{site.baseurl}}/images/off.png" width="60" height="Auto" style="margin-left: auto; margin-right: auto;">
                    <button type="button" id="buttR{{ i }}" onclick="javascript:toggleBitR({{ i }})">Turn on</button>
                </td>
                {% endfor %}
            </tr>
            <tr>
                {% comment %}Value of bit{% endcomment %}
                {% for i in (0..bits) %}
                <td><input type='text' id="digitR{{ i }}" Value="0" size="1" readonly></td>
                {% endfor %}
            </tr>
            </table>
            <table class="table">
            <tr>
                {% comment %}Build many bits{% endcomment %}
                {% for i in (0..bits) %}
                <td><img class="img-responsive py-3" id="bulbG{{ i }}" src="{{site.baseurl}}/images/off.png" width="60" height="Auto" style="margin-left: auto; margin-right: auto;">
                    <button type="button" id="buttG{{ i }}" onclick="javascript:toggleBitG({{ i }})">Turn on</button>
                </td>
                {% endfor %}
            </tr>
            <tr>
                {% comment %}Value of bit{% endcomment %}
                {% for i in (0..bits) %}
                <td><input type='text' id="digitG{{ i }}" Value="0" size="1" readonly></td>
                {% endfor %}
            </tr>
            </table>
            <table class="table">
            <tr>
                {% comment %}Build many bits{% endcomment %}
                {% for i in (0..bits) %}
                <td><img class="img-responsive py-3" id="bulbB{{ i }}" src="{{site.baseurl}}/images/off.png" width="60" height="Auto" style="margin-left: auto; margin-right: auto;">
                    <button type="button" id="buttB{{ i }}" onclick="javascript:toggleBitB({{ i }})">Turn on</button>
                </td>
                {% endfor %}
            </tr>
            <tr>
                {% comment %}Value of bit{% endcomment %}
                {% for i in (0..bits) %}
                <td><input type='text' id="digitB{{ i }}" Value="0" size="1" readonly></td>
                {% endfor %}
            </tr>
            </table>
        </div>
    </div>
</div>

<script>
    const BITS = {{ BITS }};
    const MAX = 2 ** BITS - 1;
    const MSG_ON = "Turn on";
    const IMAGE_ON = "{{site.baseurl}}/images/on.png";
    const MSG_OFF = "Turn off";
    const IMAGE_OFF = "{{site.baseurl}}/images/off.png";

    function binaryNumbering() {
        let number = "";
        for(let i = 0; i < BITS; i++) {
        number = document.getElementById('bitNumber' + i).value;
        }
    }

    // return string with current value of each bit
    function getBits() {
        let bits = "";
        for(let i = 0; i < BITS; i++) {
        bits = bits + document.getElementById('digit' + i).value;
        }
        return bits;
    }
    function getBitsR() {
        let bits = "";
        for(let i = 0; i < BITS; i++) {
        bits = bits + document.getElementById('digitR' + i).value;
        }
        return bits;
    }
    function getBitsG() {
        let bits = "";
        for(let i = 0; i < BITS; i++) {
        bits = bits + document.getElementById('digitG' + i).value;
        }
        return bits;
    }
    function getBitsB() {
        let bits = "";
        for(let i = 0; i < BITS; i++) {
        bits = bits + document.getElementById('digitB' + i).value;
        }
        return bits;
    }

    function binToChar(bin) {
        let dec = parseInt(bin, 2).toString();
        console.log(dec);
        var chr = String.fromCharCode(dec);
        return chr;
    }
    // setter for DOM values
    function setConversions(binary) {
        document.getElementById('binary').innerHTML = binary;
        // Octal conversion
        document.getElementById('octal').innerHTML = parseInt(binary, 2).toString(8);
        // Hexadecimal conversion
        document.getElementById('hexadecimal').innerHTML = parseInt(binary, 2).toString(16);
        // Decimal conversion
        document.getElementById('decimal').innerHTML = parseInt(binary, 2).toString();
        let dec = parseInt(document.getElementById('decimal').innerHTML);
        if (dec >= 32 && dec <= 255) {
        document.getElementById('character').innerHTML = binToChar(binary);
        }
        else {
            document.getElementById('character').innerHTML = "Can't Print";
        }
    }
    function setConversionsR(binary) {
        document.getElementById('binR').innerHTML = binary;
        // Hexadecimal conversion
        document.getElementById('hexR').innerHTML = parseInt(binary, 2).toString(16).padStart(2, '0');
        // Decimal conversion
        document.getElementById('decR').innerHTML = parseInt(binary, 2).toString();
        document.getElementById('color').style.backgroundColor = setRGB();
    }
    function setConversionsG(binary) {
        document.getElementById('binG').innerHTML = binary;
        // Hexadecimal conversion
        document.getElementById('hexG').innerHTML = parseInt(binary, 2).toString(16).padStart(2, '0');
        // Decimal conversion
        document.getElementById('decG').innerHTML = parseInt(binary, 2).toString();
        document.getElementById('color').style.backgroundColor = setRGB();
    }
    function setConversionsB(binary) {
        document.getElementById('binB').innerHTML = binary;
        // Hexadecimal conversion
        document.getElementById('hexB').innerHTML = parseInt(binary, 2).toString(16).padStart(2, '0');
        // Decimal conversion
        document.getElementById('decB').innerHTML = parseInt(binary, 2).toString();
        document.getElementById('color').style.backgroundColor = setRGB();
    }
    //
    function decimal_2_base(decimal, base) {
        let conversion = "";
        // loop to convert to base
        do {
        let digit = decimal % base;
        conversion = "" + digit + conversion; // what does this do?
        decimal = ~~(decimal / base);         // what does this do?
        } while (decimal > 0);                  // why while at the end? what is ~~?
        // loop to pad with zeros
        if (base === 2) {                        // only pad for binary conversions
        for (let i = 0; conversion.length < BITS; i++) {
            conversion = "0" + conversion;
        }
        }
        return conversion;
    }

    // toggle selected bit and recalculate
    function toggleBit(i) {
        //alert("Digit action: " + i );
        const dig = document.getElementById('digit' + i);
        const image = document.getElementById('bulb' + i);
        const butt = document.getElementById('butt' + i);
        // Change digit and visual
        if (image.src.match(IMAGE_ON)) {
        dig.value = 0;
        image.src = IMAGE_OFF;
        butt.innerHTML = MSG_ON;
        } else {
        dig.value = 1;
        image.src = IMAGE_ON;
        butt.innerHTML = MSG_OFF;
        }
        // Binary numbers
        const binary = getBits();
        setConversions(binary);
    }
    function toggleBitR(i) {
        //alert("Digit action: " + i );
        const dig = document.getElementById('digitR' + i);
        const image = document.getElementById('bulbR' + i);
        const butt = document.getElementById('buttR' + i);
        // Change digit and visual
        if (image.src.match(IMAGE_ON)) {
        dig.value = 0;
        image.src = IMAGE_OFF;
        butt.innerHTML = MSG_ON;
        } else {
        dig.value = 1;
        image.src = IMAGE_ON;
        butt.innerHTML = MSG_OFF;
        }
        // Binary numbers
        const binary = getBitsR();
        setConversionsR(binary);
    }
    function toggleBitG(i) {
        //alert("Digit action: " + i );
        const dig = document.getElementById('digitG' + i);
        const image = document.getElementById('bulbG' + i);
        const butt = document.getElementById('buttG' + i);
        // Change digit and visual
        if (image.src.match(IMAGE_ON)) {
        dig.value = 0;
        image.src = IMAGE_OFF;
        butt.innerHTML = MSG_ON;
        } else {
        dig.value = 1;
        image.src = IMAGE_ON;
        butt.innerHTML = MSG_OFF;
        }
        // Binary numbers
        const binary = getBitsG();
        setConversionsG(binary);
    }
    function toggleBitB(i) {
        //alert("Digit action: " + i );
        const dig = document.getElementById('digitB' + i);
        const image = document.getElementById('bulbB' + i);
        const butt = document.getElementById('buttB' + i);
        // Change digit and visual
        if (image.src.match(IMAGE_ON)) {
        dig.value = 0;
        image.src = IMAGE_OFF;
        butt.innerHTML = MSG_ON;
        } else {
        dig.value = 1;
        image.src = IMAGE_ON;
        butt.innerHTML = MSG_OFF;
        }
        // Binary numbers
        const binary = getBitsB();
        setConversionsB(binary);
    }
    // add is positive integer, subtract is negative integer
    function add(n) {
        let binary = getBits();
        // convert to decimal and do math
        let decimal = parseInt(binary, 2);
        if (n > 0) {  // PLUS
        decimal = MAX === decimal ? 0 : decimal += n; // OVERFLOW or PLUS
        } else  {     // MINUS
        decimal = 0 === decimal ? MAX : decimal += n; // OVERFLOW or MINUS
        }
        // convert the result back to binary
        binary = decimal_2_base(decimal, 2);
        // update conversions
        setConversions(binary);
        // update bits
        for (let i = 0; i < binary.length; i++) {
        let digit = binary.substr(i, 1);
        document.getElementById('digit' + i).value = digit;
        if (digit === "1") {
            document.getElementById('bulb' + i).src = IMAGE_ON;
            document.getElementById('butt' + i).innerHTML = MSG_OFF;
        } else {
            document.getElementById('bulb' + i).src = IMAGE_OFF;
            document.getElementById('butt' + i).innerHTML = MSG_ON;
        }
        }
    }
    function addR(n) {
        let binary = getBitsR();
        // convert to decimal and do math
        let decimal = parseInt(binary, 2);
        if (n > 0) {  // PLUS
        decimal = MAX === decimal ? 0 : decimal += n; // OVERFLOW or PLUS
        } else  {     // MINUS
        decimal = 0 === decimal ? MAX : decimal += n; // OVERFLOW or MINUS
        }
        // convert the result back to binary
        binary = decimal_2_base(decimal, 2);
        // update conversions
        setConversionsR(binary);
        // update bits
        for (let i = 0; i < binary.length; i++) {
        let digit = binary.substr(i, 1);
        document.getElementById('digitR' + i).value = digit;
        if (digit === "1") {
            document.getElementById('bulbR' + i).src = IMAGE_ON;
            document.getElementById('buttR' + i).innerHTML = MSG_OFF;
        } else {
            document.getElementById('bulbR' + i).src = IMAGE_OFF;
            document.getElementById('buttR' + i).innerHTML = MSG_ON;
        }
        }
    }
    function addG(n) {
        let binary = getBitsG();
        // convert to decimal and do math
        let decimal = parseInt(binary, 2);
        if (n > 0) {  // PLUS
        decimal = MAX === decimal ? 0 : decimal += n; // OVERFLOW or PLUS
        } else  {     // MINUS
        decimal = 0 === decimal ? MAX : decimal += n; // OVERFLOW or MINUS
        }
        // convert the result back to binary
        binary = decimal_2_base(decimal, 2);
        // update conversions
        setConversionsG(binary);
        // update bits
        for (let i = 0; i < binary.length; i++) {
        let digit = binary.substr(i, 1);
        document.getElementById('digitG' + i).value = digit;
        if (digit === "1") {
            document.getElementById('bulbG' + i).src = IMAGE_ON;
            document.getElementById('buttG' + i).innerHTML = MSG_OFF;
        } else {
            document.getElementById('bulbG' + i).src = IMAGE_OFF;
            document.getElementById('buttG' + i).innerHTML = MSG_ON;
        }
        }
    }
    function addB(n) {
        let binary = getBitsB();
        // convert to decimal and do math
        let decimal = parseInt(binary, 2);
        if (n > 0) {  // PLUS
        decimal = MAX === decimal ? 0 : decimal += n; // OVERFLOW or PLUS
        } else  {     // MINUS
        decimal = 0 === decimal ? MAX : decimal += n; // OVERFLOW or MINUS
        }
        // convert the result back to binary
        binary = decimal_2_base(decimal, 2);
        // update conversions
        setConversionsB(binary);
        // update bits
        for (let i = 0; i < binary.length; i++) {
        let digit = binary.substr(i, 1);
        document.getElementById('digitB' + i).value = digit;
        if (digit === "1") {
            document.getElementById('bulbB' + i).src = IMAGE_ON;
            document.getElementById('buttB' + i).innerHTML = MSG_OFF;
        } else {
            document.getElementById('bulbB' + i).src = IMAGE_OFF;
            document.getElementById('buttB' + i).innerHTML = MSG_ON;
        }
        }
    }
    function setRGB() {
        let R = document.getElementById('hexR').innerHTML;
        let G = document.getElementById('hexG').innerHTML;
        let B = document.getElementById('hexB').innerHTML;
        let color_code = "#" + R + G + B;
        console.log(color_code)
        return color_code
    }
    var sliderR = document.getElementById("sliderR");
        sliderR.addEventListener("wheel", function(e){
        if (e.deltaY < 0){
            sliderR.valueAsNumber += 1;
            addR(1)
        }else{
            sliderR.value -= 1;
            addR(-1)
        }
        e.preventDefault();
        e.stopPropagation();
    })
    var sliderG = document.getElementById("sliderG");
        sliderG.addEventListener("wheel", function(e){
        if (e.deltaY < 0){
            sliderG.valueAsNumber += 1;
            addG(1)
        }else{
            sliderG.value -= 1;
            addG(-1)
        }
        e.preventDefault();
        e.stopPropagation();
    })
    var sliderB = document.getElementById("sliderB");
        sliderB.addEventListener("wheel", function(e){
        if (e.deltaY < 0){
            sliderB.valueAsNumber += 1;
            addB(1)
        }else{
            sliderB.value -= 1;
            addB(-1)
        }
        e.preventDefault();
        e.stopPropagation();
    })
</script>