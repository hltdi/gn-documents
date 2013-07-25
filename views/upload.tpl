%rebase layout

<div class="header">
    	<span id="title">Tahekami</span>
</div>
<form action="upload" method="post" enctype="multipart/form-data">	
    <div id="content">
    	<h1>Subir un Documento</h1>
    	<div id="form">
    		<div class="form-section">
    			<h3>T&iacute;tulo</h3>
        		<input class="input-long" name="titulo-input" type="text" value="Escribe aquí el título del documento" size="480" maxlength="500" />
    		</div>
       		<div class="form-section">
        		<h3>Idioma</h3>
          		<ul id="select-upload-lang">
          			<li><input name="castellano" type="radio" value="castellano" checked="checked"/> Castellano</li>	
          			<li><input name="guarani" type="radio" value="guarani" /> Guaran&iacute;</li>
            		<li><input name="bilingue" type="radio" value="castellano y guarani" /> Castellano y Guaran&iacute;</li>
          		</ul>
        	</div>
			<div class="form-section">
        		<h3>Archivo(s)</h3>
          		<div class="form-sub-section">
          			<span class="inline-title">Castellano: </span><input name="uploadSpanish" type="file"/>
           		</div>
           		<div class="form-sub-section">
            		<span class="inline-title">Guaran&iacute;: </span><input name="uploadGuarani" type="file"/>
            	</div>
          	</div>
          
          	<div class="form-section">
          		<h3>Etiquetas (separadas por coma)</h3>
            	<input class="input-long" name="tags" type="text" value="Ej... literatura, poesía, roa bastos" />
          	</div>
          	
          	<div class="form-section">
          		<h3>Informaci&oacute;n adicional</h3>
            	<div class="form-sub-section">
            	<span class="inline-title">Autor: </span>
              	<input class="input-inline-long" name="autor" type="text" />
            </div>
            <div class="form-sub-section">
            	<span class="inline-title">Instituto: </span>
              	<input class="input-inline-long" name="autor" type="text" />
            </div>
            <div class="form-sub-section">
            	<input name="descargar" type="checkbox" value="desargar" checked="checked" />
              	<span> Permitir la descarga</span>
            </div>
            <div>
          		<button id="submit-document-button" class="submit-button" name="search-button" value="Buscar" type="submit"><span id="search-button-text">Enviar</span></button>
          	</div>
        </div>
	</div>	
</form>

<!-- js files -->
<script src="js/upload.js"></script>
<script src="js/jquery.form.min.js"></script>
 
	
