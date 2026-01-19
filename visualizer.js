const CELL = 45;

// Hardcoded matrices
let A = [
    [1, 2],
    [3, 4]
];
let B = [
    [2, 0],
    [1, 2]
];
let C = [];
let i = 0, j = 0;

const aRows = document.getElementById("aRows");
const aCols = document.getElementById("aCols");
const bRows = document.getElementById("bRows");
const bCols = document.getElementById("bCols");
const nextBtn = document.getElementById("nextBtn");
const error = document.getElementById("error");

// Apply dimension change on input typed
[aRows, aCols, bRows, bCols].forEach(input =>
    input.addEventListener("input", resizeMatrices)
);

resizeMatrices();

// Reset & define the matrices according to current configuration
function resizeMatrices() {
    // Do not redefine matrix when input is invalid
    if (!aRows.value || !aCols.value || !bRows.value || !bCols.value) return;
    A = resize(A, +aRows.value, +aCols.value);
    B = resize(B, +bRows.value, +bCols.value);
    resetResult();
    renderAll();
}

function resize(M, r, c) {
    const res = [];
    for (let i = 0; i < r; i++) {
        res[i] = [];
        for (let j = 0; j < c; j++) {
            // Keep the original values in the cells, otherwise 0
            res[i][j] = M?.[i]?.[j] ?? 0;
        }
    }
    return res;
}

function resetResult() {
    C = Array.from({ length: A.length },
        () => Array(B[0].length).fill(null));
    i = j = 0;
    nextBtn.disabled = false;
}

// Rendering code

function renderAll() {
    renderMatrix(A, "matrixA", true);
    renderMatrix(B, "matrixB", true);
    renderMatrix(C, "matrixC", false);
}

function renderMatrix(M, id, editable) {
    const e = document.getElementById(id);
    e.innerHTML = "";
    e.style.gridTemplateColumns = `repeat(${M[0].length}, ${CELL}px)`;

    M.forEach((row, r) => {
        row.forEach((v, c) => {
            if (editable) {
                const input = document.createElement("input");
                input.type = "number";
                input.value = v;
                input.className = "cell";
                input.oninput = () => {
                    M[r][c] = +input.value;
                    resetResult();
                    renderResult();
                };
                e.appendChild(input);
            } else {
                const div = document.createElement("div");
                div.className = "resultCell";
                div.textContent = v ?? "";
                e.appendChild(div);
            }
        });
    });
}

function canMultiply() {
    return A[0].length === B.length;
}

async function nextStep() {
    if (!canMultiply()) {
        error.textContent = "Multiplication undefined (A cols ≠ B rows).";
        return;
    }

    nextBtn.disabled = true;
    error.textContent = "";
    await animateDotProduct(i, j);
    nextBtn.disabled = false;
    computeResult(i, j);
    advance();
}

function computeResult(r, c) {
    let sum = 0;
    for (let k = 0; k < A[0].length; k++)
        sum += A[r][k] * B[k][c];
    C[r][c] = sum;
    renderMatrix(C, "matrixC", false);
}

function advance() {
    j++;
    if (j >= C[0].length) {
        j = 0;
        i++;
    }
    if (i >= C.length) {
        nextBtn.disabled = true;
        i = j = 0;
    }
}

async function animateDotProduct(row, col) {
    const anim = document.createElement("div");
    anim.className = "animatedColumn";

    for (let r = 0; r < B.length; r++) {
        const d = document.createElement("div");
        d.className = "cell";
        d.textContent = B[r][col];
        anim.appendChild(d);
    }

    document.body.appendChild(anim);

    // Target row in A
    const targetCell = document.querySelectorAll("#matrixA .cell")[row * A[0].length];
    const targetRect = targetCell.getBoundingClientRect();

    // Column in B
    const bCells = document.querySelectorAll("#matrixB .cell");
    const colStartCell = bCells[col];
    const colRect = colStartCell.getBoundingClientRect();

    anim.style.left = colRect.left + "px";
    anim.style.top = targetRect.top + "px";

    await sleep(50);

    anim.style.transform = "rotate(-90deg)";
    await sleep(900);

    anim.style.left = targetRect.left + "px";
    anim.style.top = targetRect.top + "px";

    pulse(row, col);
    await sleep(600);
    anim.remove();
}

// Highlight the given row and column for a brief moment
function pulse(row, col) {
    document.querySelectorAll("#matrixA .cell").forEach((c, i) => {
        if (Math.floor(i / A[0].length) === row)
            c.classList.add("pulse");
    });

    document.querySelectorAll("#matrixB .cell").forEach((c, i) => {
        if (i % B[0].length === col)
            c.classList.add("pulse");
    });

    setTimeout(() =>
        document.querySelectorAll(".pulse")
            .forEach(c => c.classList.remove("pulse")), 600);
}


function skipAll() {
    if (!canMultiply()) return;
    for (let r = 0; r < C.length; r++)
        for (let c = 0; c < C[0].length; c++)
            computeResult(r, c);
    nextBtn.disabled = true;
}

function swap() {
    [A, B] = [B, A];
    resizeMatrices();
}

function sleep(ms) {
    return new Promise(r => setTimeout(r, ms));
}