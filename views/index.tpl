%rebase layout
		
<div id="logo-container" class="center">
    <span id="logo-text">TAHEKAMI</span>
    <br/>
    <span>5.341 documentos(ver Catálogo)</span>
    <br />
</div> <!--logo-container-->

<div id="search-form" class="center">
    <input id="search-input" name="search-input" type="text"
    ng-model="query"
    ng-init="query='Escribe aquí las palabras clave del documento que desees buscar'"
    ng-click="query=''"
    size="454" />
    <br />
    <div id="select-lang">
        <div class="centerbox">
        <span id="select-lang-text">Buscar documentos en:</span><br/>
        <label class="frontpage"><input class="check" name="guarani" type="checkbox" value="" checked="checked"/>
        Guaraní 
        </label>
        <br/>
        <label class="frontpage"><input class="check" name="spanish" type="checkbox" value="" checked="checked"/>
        Castellano 
        </label>
        </div> <!--centerbox-->
    </div> <!--select-lang-->
    <div>
      <button class="submit-button" name="search-button" type="submit" />
      <span id="search-button-text">Buscar</span>
      </button>
    </div> <!--submit-button-->
</div> <!--search-form-->
