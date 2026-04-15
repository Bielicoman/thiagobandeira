#!/usr/bin/env python3
# Script to replace portfolio grid in index.html
import re

NEW_GRID = '''        <div class="projects-grid">

            <!-- 1 · Performance -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="DXB_N4-r-H8" data-title="Aula Magna 2026" data-client="UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/DXB_N4-r-H8/mqdefault.jpg" alt="Aula Magna 2026" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">LIVE</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Multicam</span>
                        <h3 class="pcard-title">Aula Magna 2026</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">MULTI-CAM</span><span class="hud-meta">UNASP</span></div>
                    </div>
                </a>
            </div>

            <!-- 2 · Documentário -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="RJpcS7dLJPQ" data-title="Sabores do Brasil" data-client="Santa Helena Alimentos">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/RJpcS7dLJPQ/mqdefault.jpg" alt="Sabores do Brasil" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">DOC MODE</span><span class="hud-tag">4K</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Sabores do Brasil</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">BRANDED</span><span class="hud-meta">EP.01</span></div>
                    </div>
                </a>
            </div>

            <!-- 3 · Cinema/Curta -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="h5vbvGte3oM" data-title="O Peso das Palavras" data-client="Entre Aspas">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/h5vbvGte3oM/mqdefault.jpg" alt="O Peso das Palavras" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">4K RAW</span><span class="hud-tag">24FPS</span></div>
                        <span class="pcard-role">Diretor | Dir. de Fotografia</span>
                        <h3 class="pcard-title">O Peso das Palavras</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">CURTA</span><span class="hud-meta">ASPECT 2.39:1</span></div>
                    </div>
                </a>
            </div>

            <!-- 4 · Performance -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="5FxSxY7iMo0" data-title="Culto de Sexta" data-client="UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/5FxSxY7iMo0/mqdefault.jpg" alt="Culto de Sexta" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">LIVE</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Culto de Sexta</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">MULTI-CAM</span><span class="hud-meta">UNASP</span></div>
                    </div>
                </a>
            </div>

            <!-- 5 · Performance -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="708nWQhWdfE" data-title="UNASP Campus EC" data-client="UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/708nWQhWdfE/mqdefault.jpg" alt="UNASP Campus EC" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">INSTITUCIONAL</span><span class="hud-tag">4K</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Operador</span>
                        <h3 class="pcard-title">UNASP Campus EC</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">LOG-C</span><span class="hud-meta">UNASP</span></div>
                    </div>
                </a>
            </div>

            <!-- 6 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="m93qBGgcTsI" data-title="Nunca \\u00c9 Tarde" data-client="Novo Tom">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/m93qBGgcTsI/mqdefault.jpg" alt="Nunca É Tarde" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">RUN</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Nunca É Tarde</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ASPECT 16:9</span><span class="hud-meta">REC.709</span></div>
                    </div>
                </a>
            </div>

            <!-- 7 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="-homFYaw7z8" data-title="Santificado" data-client="Novo Tom">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/-homFYaw7z8/mqdefault.jpg" alt="Santificado" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">CAM A</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Santificado</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ANAMORPHIC</span><span class="hud-meta">LOG-C</span></div>
                    </div>
                </a>
            </div>

            <!-- 8 · Performance -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="g73nHqXJY-M" data-title="Arte Na Mesa #06" data-client="UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/g73nHqXJY-M/mqdefault.jpg" alt="Arte Na Mesa #06" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">PODCAST</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Arte Na Mesa #06</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">MULTI-CAM</span><span class="hud-meta">UNASP</span></div>
                    </div>
                </a>
            </div>

            <!-- 9 · Performance -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="vP7nbYS_DgY" data-title="Arte Na Mesa #05" data-client="UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/vP7nbYS_DgY/mqdefault.jpg" alt="Arte Na Mesa #05" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">PODCAST</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Arte Na Mesa #05</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">MULTI-CAM</span><span class="hud-meta">UNASP</span></div>
                    </div>
                </a>
            </div>

            <!-- 10 · Performance -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="yh_ZZTQN3-I" data-title="Arte Na Mesa #02" data-client="UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/yh_ZZTQN3-I/mqdefault.jpg" alt="Arte Na Mesa #02" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">PODCAST</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Arte Na Mesa #02</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">MULTI-CAM</span><span class="hud-meta">UNASP</span></div>
                    </div>
                </a>
            </div>

            <!-- 11 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="wl8Lc5n71jQ" data-title="Uma Pátria" data-client="Coro de Licenciatura em Música">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/wl8Lc5n71jQ/mqdefault.jpg" alt="Uma Pátria" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Uma Pátria</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ASPECT 16:9</span><span class="hud-meta">REC.709</span></div>
                    </div>
                </a>
            </div>

            <!-- 12 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="vptKdSzSw0Y" data-title="NEle (Live Session)" data-client="Coral Canção Jovem">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/vptKdSzSw0Y/mqdefault.jpg" alt="NEle Live Session" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">LIVE SESSION</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">NEle</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">LIVE SESSION</span><span class="hud-meta">HDR</span></div>
                    </div>
                </a>
            </div>

            <!-- 13 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="THiRhQtPTKw" data-title="As Estrelas Nunca Deixam de Brilhar" data-client="Coral Canção Jovem">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/THiRhQtPTKw/mqdefault.jpg" alt="As Estrelas Nunca Deixam de Brilhar" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">CAM A</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">As Estrelas</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ASPECT 16:9</span><span class="hud-meta">LOG-C</span></div>
                    </div>
                </a>
            </div>

            <!-- 14 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="GevwTHA0SDA" data-title="Oh, Que Esperança" data-client="Orquestra Sinfônica UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/GevwTHA0SDA/mqdefault.jpg" alt="Oh, Que Esperança" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">RUN</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Oh, Que Esperança</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">SINFÔNICO</span><span class="hud-meta">REC.709</span></div>
                    </div>
                </a>
            </div>

            <!-- 15 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="hYmDMIVQ4Og" data-title="Oh, Fronte Ensanguentada" data-client="Orquestra Sinfônica UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/hYmDMIVQ4Og/mqdefault.jpg" alt="Oh, Fronte Ensanguentada" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">CAM A</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Oh, Fronte</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">SINFÔNICO</span><span class="hud-meta">LOG-C</span></div>
                    </div>
                </a>
            </div>

            <!-- 16 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="LPSdRoq1EJs" data-title="Bem Junto a Cristo" data-client="Orquestra Sinfônica UNASP">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/LPSdRoq1EJs/mqdefault.jpg" alt="Bem Junto a Cristo" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Bem Junto a Cristo</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">SINFÔNICO</span><span class="hud-meta">HDR</span></div>
                    </div>
                </a>
            </div>

            <!-- 17 · Documentário -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="0gXPzkrl0cA" data-title="Herói da Fé (Making Of)" data-client="UNASP 75 Anos">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/0gXPzkrl0cA/mqdefault.jpg" alt="Herói da Fé Making Of" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">MAKING OF</span><span class="hud-tag">DOC</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Herói da Fé</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">SHUTTER 180°</span><span class="hud-meta">ISO 800</span></div>
                    </div>
                </a>
            </div>

            <!-- 18 · Documentário -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="WKTqguahTMU" data-title="A Terra Santa" data-client="Museu de Arqueologia Bíblica">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/WKTqguahTMU/mqdefault.jpg" alt="A Terra Santa" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">DOC MODE</span><span class="hud-tag">4K</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">A Terra Santa</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">DOCUMENTÁRIO</span><span class="hud-meta">LOG-C</span></div>
                    </div>
                </a>
            </div>

            <!-- 19 · Cinema/Curta -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="p6SIYQ2c2Bw" data-title="Bárbara (Curta)" data-client="Califórnia Dreams">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/p6SIYQ2c2Bw/mqdefault.jpg" alt="Bárbara Curta Metragem" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">PRORES 4444</span><span class="hud-tag">24FPS</span></div>
                        <span class="pcard-role">Diretor | Dir. de Fotografia</span>
                        <h3 class="pcard-title">Bárbara</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">CURTA</span><span class="hud-meta">16MM LOOK</span></div>
                    </div>
                </a>
            </div>

            <!-- 20 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="WeBx8Ewkm4I" data-title="Meu Respirar" data-client="Gabriella Stehling">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/WeBx8Ewkm4I/mqdefault.jpg" alt="Meu Respirar" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">RUN</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Meu Respirar</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ANAMORPHIC</span><span class="hud-meta">CAM A</span></div>
                    </div>
                </a>
            </div>

            <!-- 21 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="rQlMRuub6vo" data-title="Jeová Jireh" data-client="Gabriella Stehling">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/rQlMRuub6vo/mqdefault.jpg" alt="Jeová Jireh" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">ACTIVE</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Jeová Jireh</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ASPECT 16:9</span><span class="hud-meta">REC.709</span></div>
                    </div>
                </a>
            </div>

            <!-- 22 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="yrkck9BhKqo" data-title="Tu És" data-client="Produção Audiovisual">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/yrkck9BhKqo/mqdefault.jpg" alt="Tu És" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">STANDBY</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Câmera</span>
                        <h3 class="pcard-title">Tu És</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">HDR 10</span><span class="hud-meta">ISO 400</span></div>
                    </div>
                </a>
            </div>

            <!-- 23 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="b1ufVsXLPt8" data-title="Ele Reviveu" data-client="Produção Audiovisual">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/b1ufVsXLPt8/mqdefault.jpg" alt="Ele Reviveu" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">SYNC</span></div>
                        <span class="pcard-role">Diretor de Produção</span>
                        <h3 class="pcard-title">Ele Reviveu</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">LENS: 50MM</span><span class="hud-meta">180° SHUTTER</span></div>
                    </div>
                </a>
            </div>

            <!-- 24 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="DAglqbQTK4c" data-title="Lembra" data-client="Kati Carvalho &amp; Communion">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/DAglqbQTK4c/mqdefault.jpg" alt="Lembra" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Produtor</span>
                        <h3 class="pcard-title">Lembra</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">WB 5600K</span><span class="hud-meta">T 2.8</span></div>
                    </div>
                </a>
            </div>

            <!-- 25 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="D43qNYNIIOA" data-title="O Melhor de Mim" data-client="Grupo Versos">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/D43qNYNIIOA/mqdefault.jpg" alt="O Melhor de Mim" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">ON</span></div>
                        <span class="pcard-role">Dir. de Fotografia | Produtor Técnico</span>
                        <h3 class="pcard-title">O Melhor de Mim</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">4:2:2 10-BIT</span><span class="hud-meta">ASPECT 2.35:1</span></div>
                    </div>
                </a>
            </div>

            <!-- 26 · Videoclipe -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="RRfgyZBCGn4" data-title="Nosso Jeito de Amar" data-client="Música">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/RRfgyZBCGn4/mqdefault.jpg" alt="Nosso Jeito de Amar" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">M. CLIPE</span><span class="hud-tag">REC</span></div>
                        <span class="pcard-role">Operador | Produtor</span>
                        <h3 class="pcard-title">Nosso Jeito de Amar</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">1080P PRO</span><span class="hud-meta">LUT: FILM</span></div>
                    </div>
                </a>
            </div>

            <!-- 27 · Cinema/Curta -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="efa_PSKMHLk" data-title="O Oráculo" data-client="Califórnia Dreams">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/efa_PSKMHLk/mqdefault.jpg" alt="O Oráculo" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">4.6K RAW</span><span class="hud-tag">24FPS</span></div>
                        <span class="pcard-role">Diretor | Dir. de Fotografia</span>
                        <h3 class="pcard-title">O Oráculo</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ASPECT 2.39:1</span><span class="hud-meta">REALITY</span></div>
                    </div>
                </a>
            </div>

            <!-- 28 · Documentário -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="D8IE251bp_E" data-title="Documentário WELL" data-client="WELL">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/D8IE251bp_E/mqdefault.jpg" alt="Documentário WELL" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">DOC MODE</span><span class="hud-tag">STBY</span></div>
                        <span class="pcard-role">Dir. Agência | Dir. Fotografia</span>
                        <h3 class="pcard-title">Documentário WELL</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">LOG-C</span><span class="hud-meta">LENS: 35MM</span></div>
                    </div>
                </a>
            </div>

            <!-- 29 · Cinema/Curta -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="Mul19Lfeo7Y" data-title="Bárbara (Alt)" data-client="Califórnia Dreams">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/Mul19Lfeo7Y/mqdefault.jpg" alt="Bárbara Alt" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">PRORES 4444</span><span class="hud-tag">FROZEN</span></div>
                        <span class="pcard-role">Diretor | Câmera</span>
                        <h3 class="pcard-title">Bárbara — Alt</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">16MM LOOK</span><span class="hud-meta">NOISE+</span></div>
                    </div>
                </a>
            </div>

            <!-- 30 · Documentário -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="NwesZCYbSx0" data-title="Cicatrizes" data-client="Califórnia Dreams">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/NwesZCYbSx0/mqdefault.jpg" alt="Cicatrizes" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">DOC MODE</span><span class="hud-tag">60FPS</span></div>
                        <span class="pcard-role">Câmera | Diretor de Produção</span>
                        <h3 class="pcard-title">Cicatrizes</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">SHUTTER 180°</span><span class="hud-meta">ISO 800</span></div>
                    </div>
                </a>
            </div>

            <!-- 31 · Documentário -->
            <div class="pcard-wrap">
                <a href="#" class="pcard fade-in" data-video-id="Mdkzm7v2vc8" data-title="VT Engenharia" data-client="VT Engenharia">
                    <div class="pcard-thumb"><img src="https://img.youtube.com/vi/Mdkzm7v2vc8/mqdefault.jpg" alt="VT Engenharia" loading="lazy" decoding="async"></div>
                    <div class="pcard-noise"></div><div class="pcard-shine"></div>
                    <div class="pcard-glass">
                        <div class="pcard-hud-top"><span class="hud-tag">4K PRO</span><span class="hud-tag">STILL</span></div>
                        <span class="pcard-role">Diretor de Fotografia</span>
                        <h3 class="pcard-title">VT Engenharia</h3>
                        <div class="pcard-hud-bottom"><span class="hud-meta">ASPECT 16:9</span><span class="hud-meta">COLOR PRO</span></div>
                    </div>
                </a>
            </div>

        </div>
    </section>'''

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of projects-grid
start_marker = '        <div class="projects-grid">'
# Find the closing of the projects section: </div>\n    </section>\n\n    <div class="section-glow-sep">
# We'll find the next section-glow-sep after projects-grid to know where projects section ends
start_idx = content.find(start_marker)
if start_idx == -1:
    print("ERROR: projects-grid start not found!")
    exit(1)

# Find the section close: look for '</section>' followed by '\n\n    <div class="section-glow-sep">'
section_close = '    </section>\n\n    <div class="section-glow-sep">'
end_idx = content.find(section_close, start_idx)
if end_idx == -1:
    print("ERROR: section close not found!")
    exit(1)

# The end of what we want to replace is end_idx + len('    </section>')
replace_end = end_idx + len('    </section>')

old_section = content[start_idx:replace_end]
print(f"Replacing {len(old_section)} chars ({old_section.count(chr(10))} lines)")

new_content = content[:start_idx] + NEW_GRID + content[replace_end:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! File written successfully.")
print(f"Old length: {len(content)}, New length: {len(new_content)}")
