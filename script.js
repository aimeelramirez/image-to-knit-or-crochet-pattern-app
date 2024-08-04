document.getElementById('uploadButton').addEventListener('click', async () => { 
    const fileInput = document.getElementById('imageUpload');
    const pixelSize = document.getElementById('pixelSize').value;
    const file = fileInput.files[0];
    const formData = new FormData();
    formData.append('image', file);
    formData.append('pixel_size', pixelSize);

    const response = await fetch('http://127.0.0.1:5000/process_image', {
      method: 'POST',
      body: formData,
    });
    const result = await response.json();

    const colors = result.colors;
    const imgBase64 = result.img_base64;

    document.getElementById('pixelatedImage').src =
      'data:image/png;base64,' + imgBase64;

      const colorGrid = document.getElementById('colorGrid');
        const rowLabels = document.getElementById('rowLabels');
        const colorList = document.getElementById('colorList');
        colorGrid.innerHTML = ''; // Clear previous colors
        rowLabels.innerHTML = ''; // Clear previous row labels
        colorList.innerHTML = ''; // Clear previous color list

        // Determine grid dimensions
        const cellSize = 10; // Default size
        const pixelData = result.pixel_data;
        const numColumns = pixelData[0].length;
        const numRows = pixelData.length;
        document.getElementById('summary').innerHTML = `<h3>Rows: ${numRows} <br/> Columns: ${numColumns} </h3>`;

        // Set grid size
        colorGrid.style.gridTemplateColumns = `repeat(${numColumns}, ${cellSize}px)`;
        colorGrid.style.gridTemplateRows = `repeat(${numRows}, ${cellSize}px)`;
        
        // Set row labels
        for (let i = 0; i < numRows; i++) {
            const rowLabel = document.createElement('span');
            rowLabel.textContent = i;
            rowLabels.appendChild(rowLabel);
        }

        // Populate the color grid and sidebar list
        function rgbToHex(r, g, b) {
            const componentToHex = c => c.toString(16).padStart(2, '0');
            return `#${componentToHex(r)}${componentToHex(g)}${componentToHex(b)}`;
        }

        pixelData.forEach((row, rowIndex) => {
            row.forEach((color, colIndex) => {
                const [r, g, b] = color;
                const colorsHex = rgbToHex(r, g, b);
                const colorName = ntc.name(colorsHex)[1];

                // Create color box in grid with tooltip
                const colorBox = document.createElement('div');
                colorBox.className = 'color-box';
                colorBox.style.backgroundColor = `rgb(${r}, ${g}, ${b})`;
                colorBox.style.width = `${cellSize}px`;
                colorBox.style.height = `${cellSize}px`;

                const tooltip = document.createElement('span');
                tooltip.className = 'tooltiptext';
                tooltip.textContent = `${colorName} (Row: ${rowIndex}, Col: ${colIndex})`;
                colorBox.appendChild(tooltip);
                colorGrid.appendChild(colorBox);

                // Create color list item
                const listItem = document.createElement('li');
                listItem.textContent = colorName;
                listItem.dataset.row = rowIndex;
                listItem.dataset.column = colIndex;
                listItem.classList.add('color-list-item');
                listItem.addEventListener('mouseover', () => {
                    listItem.textContent = `${colorName} (Row: ${rowIndex}, Col: ${colIndex})`;
                    document.getElementById('patternOutput').innerHTML=`<h3>${tooltip.textContent}</h3>`

                });
                listItem.addEventListener('mouseout', () => {
                    listItem.textContent = colorName;
                });
                listItem.addEventListener('click', () => {
                    document.querySelectorAll('.color-list-item').forEach(item => item.classList.remove('selected'));
                    listItem.classList.add('selected');
                    document.getElementById('patternOutput').innerHTML=`<h2>${tooltip.textContent}</h2>`

                });
                colorList.appendChild(listItem);
            });
        });
    });