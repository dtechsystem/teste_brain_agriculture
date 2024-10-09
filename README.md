<h1>API e Dashboard para Gestão de Produtores Rurais</h1>
<p>Este projeto consiste em um sistema completo para gerenciamento de produtores, fazendas e culturas agrícolas, com um <strong>dashboard interativo</strong> que exibe dados em gráficos e uma <strong>API</strong> protegida por autenticação JWT para integrações externas.</p>
<h2>🛠️ Tecnologias Utilizadas</h2>
<ul>
   <li><strong>Django</strong>: Framework web principal, utilizado para gerenciar tanto o dashboard quanto a API.</li>
   <li><strong>Django REST Framework (DRF)</strong>: Implementação da API.</li>
   <li><strong>PostgreSQL</strong>: Banco de dados relacional utilizado, gerenciado via Docker.</li>
   <li><strong>Docker</strong>: Gerenciamento de containers, com imagens separadas para o <strong>backend</strong> (Python) e o <strong>banco de dados</strong> (PostgreSQL).</li>
   <li><strong>Bootstrap</strong>: Framework CSS utilizado para criar o layout do dashboard.</li>
   <li><strong>Chart.js</strong>: Biblioteca JavaScript utilizada para exibição de gráficos interativos (pizza).</li>
   <li><strong>jQuery &amp; AJAX</strong>: Responsáveis pelas requisições assíncronas de dados para os gráficos e outras partes dinâmicas da interface.</li>
    <li><a href="http://198.50.210.247:8000/">Acesse o MVP do Dashboard</a> | Usuário: admin | Senha: admin</li>
</ul>
<h2>🚀 Funcionalidades Principais</h2>
<ol>
   <li>
      <p><strong>Dashboard Interativo</strong>:</p>
      <ul>
         <li>Exibe gráficos de distribuição de produtores, fazendas e culturas por estado, além do uso total do solo (área total, agriculturável e vegetação).</li>
         <li>Dados geridos pelo ORM do Django e renderizados no frontend com <strong>Chart.js</strong>.</li>
         <li>Requisições assíncronas feitas com <strong>AJAX</strong> para garantir a atualização dinâmica dos gráficos sem recarregar a página.</li>
      </ul>
   </li>
   <li>
      <p><strong>API RESTful</strong>:</p>
      <ul>
         <li>CRUD completo para <code>Produtores</code>, <code>Fazendas</code> e <code>Culturas</code>.</li>
         <li>Endpoints autenticados via <strong>JWT</strong>.</li>
         <li>Relatórios podem ser acessados via a API, com rotas específicas para dados agrupados por estado, cultura e uso do solo.</li>
         <li>Dados podem ser consultados e manipulados via requisições <strong>GET</strong>, <strong>POST</strong>, <strong>PUT</strong> e <strong>DELETE</strong>.</li>
      </ul>
   </li>
   <li>
      <p><strong>Testes Automatizados</strong>:</p>
      <ul>
         <li>Foram criados <strong>testes unitários</strong> usando dados <strong>mockados</strong> para validação das funcionalidades críticas, como criação, atualização e exclusão de produtores, fazendas e culturas.</li>
         <li>Testes também cobrem a geração de relatórios no dashboard.</li>
      </ul>
   </li>
</ol>
<h2>📄 Endpoints da API</h2>
<table>
   <thead>
      <tr>
         <th>Método</th>
         <th>Endpoint</th>
         <th>Descrição</th>
      </tr>
   </thead>
   <tbody>
      <tr>
         <td><code>POST</code></td>
         <td><code>/api/produtores/</code></td>
         <td>Cria um novo produtor</td>
      </tr>
      <tr>
         <td><code>GET</code></td>
         <td><code>/api/produtores/</code></td>
         <td>Lista todos os produtores</td>
      </tr>
      <tr>
         <td><code>PUT</code></td>
         <td><code>/api/produtores/&lt;id&gt;/</code></td>
         <td>Atualiza as informações de um produtor específico</td>
      </tr>
      <tr>
         <td><code>DELETE</code></td>
         <td><code>/api/produtores/&lt;id&gt;/</code></td>
         <td>Deleta um produtor específico</td>
      </tr>
      <tr>
         <td><code>POST</code></td>
         <td><code>/api/fazendas/</code></td>
         <td>Cria uma nova fazenda</td>
      </tr>
      <tr>
         <td><code>GET</code></td>
         <td><code>/api/fazendas/</code></td>
         <td>Lista todas as fazendas</td>
      </tr>
      <tr>
         <td><code>PUT</code></td>
         <td><code>/api/fazendas/&lt;id&gt;/</code></td>
         <td>Atualiza as informações de uma fazenda específica</td>
      </tr>
      <tr>
         <td><code>DELETE</code></td>
         <td><code>/api/fazendas/&lt;id&gt;/</code></td>
         <td>Deleta uma fazenda específica</td>
      </tr>
      <tr>
         <td><code>POST</code></td>
         <td><code>/api/culturas/</code></td>
         <td>Cria uma nova cultura</td>
      </tr>
      <tr>
         <td><code>GET</code></td>
         <td><code>/api/culturas/</code></td>
         <td>Lista todas as culturas</td>
      </tr>
      <tr>
         <td><code>PUT</code></td>
         <td><code>/api/culturas/&lt;id&gt;/</code></td>
         <td>Atualiza as informações de uma cultura específica</td>
      </tr>
      <tr>
         <td><code>DELETE</code></td>
         <td><code>/api/culturas/&lt;id&gt;/</code></td>
         <td>Deleta uma cultura específica</td>
      </tr>
      <tr>
         <td><code>GET</code></td>
         <td><code>/api/dashboard/</code></td>
         <td>Exibe dados agregados de fazendas e culturas por estado</td>
      </tr>
      <tr>
         <td><code>POST</code></td>
         <td><code>/api/token/</code></td>
         <td>Gera o token JWT</td>
      </tr>
      <tr>
         <td><code>POST</code></td>
         <td><code>/api/token/refresh/</code></td>
         <td>Atualiza o token JWT</td>
      </tr>
   </tbody>
</table>
<h2>📊 Dashboard - Uso do Solo e Dados Agrícolas</h2>
<p>O dashboard exibe:</p>
<ul>
   <li>Distribuição de fazendas por estado.</li>
   <li>Proporção de diferentes culturas plantadas.</li>
   <li>Relatório do uso total do solo (área total, área agriculturável e vegetação).</li>
</ul>
<h3>Gráficos Utilizados:</h3>
<ul>
   <li><strong>Gráfico de Pizza</strong> para representar a distribuição de culturas.</li>
   <li><strong>Gráfico de Barras</strong> para o uso do solo.</li>
   <li><strong>Gráfico de Linhas</strong> para o histórico de produções (opcional, pode ser implementado conforme necessidade).</li>
</ul>
<h2>🧪 Testes Unitários</h2>
<p>Para garantir a estabilidade da aplicação, implementamos testes unitários abrangentes. Os testes cobrem:</p>
<ul>
   <li>Criação, atualização e exclusão de produtores, fazendas e culturas.</li>
   <li>Verificação de erros de validação, como <strong>CPF/CNPJ inválidos</strong> e <strong>duplicidade de registros</strong>.</li>
   <li>Testes de integração da API com a exibição dos dados no dashboard.</li>
</ul>
<h3>Executando os Testes</h3>
<pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg></button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">docker-compose run brainag python manage.py <span class="hljs-built_in">test</span>
</code></div></div></pre>
<h2>🐳 Como Rodar com Docker</h2>
<h3>Pré-requisitos:</h3>
<ul>
   <li><a rel="noopener" target="_new" style="--streaming-animation-state: var(--batch-play-state-1); --animation-rate: var(--batch-play-rate-1);" href="https://www.docker.com/"><span style="--animation-count: 4; --streaming-animation-state: var(--batch-play-state-2);">Docker</span></a> instalado.</li>
</ul>
<h3>Passo a Passo:</h3>
<ol>
   <li>
      <p>Clone o repositório:</p>
      <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg></button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">git <span class="hljs-built_in">clone</span> https://github.com/seu-usuario/seu-repositorio.git
<span class="hljs-built_in">cd</span> seu-repositorio
</code></div></div></pre>
   </li>
   <li>
      <p>Crie e suba os containers Docker (API e PostgreSQL):</p>
      <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg></button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">docker-compose up --build
</code></div></div></pre>
   </li>
   <li>
      <p>Acesse a aplicação:</p>
      <ul>
         <li>O <strong>backend</strong> (Django) estará rodando em: <code>http://localhost:8000/</code>.</li>
         <li>O <strong>dashboard</strong> estará acessível via o frontend na mesma URL.</li>
      </ul>
   </li>
   <li>
      <p>Realize migrações e crie um superusuário para acessar o admin:</p>
      <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg></button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">docker-compose <span class="hljs-built_in">run</span> brainag python manage.py migrate
docker-compose <span class="hljs-built_in">run</span> brainag python manage.py createsuperuser
</code></div></div></pre>
   </li>
</ol>
<h2>🛡️ Autenticação JWT</h2>
<p>Para acessar a API, é necessário realizar a autenticação via JWT. Siga os passos abaixo para obter o token:</p>
<ol>
   <li>
      <p><strong>Obter Token</strong>:</p>
      <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9"></div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg></button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-">POST /api/token/
{
  <span class="hljs-string">"username"</span>: <span class="hljs-string">"seu-usuario"</span>,
  <span class="hljs-string">"password"</span>: <span class="hljs-string">"sua-senha"</span>
}
</code></div></div></pre>
   </li>
   <li>
      <p><strong>Usar o Token</strong> em requisições autenticadas:
         Inclua o token no cabeçalho:
      </p>
      <pre class="!overflow-visible"><div class="dark bg-gray-950 contain-inline-size rounded-md border-[0.5px] border-token-border-medium relative"><div class="flex items-center text-token-text-secondary bg-token-main-surface-secondary px-4 py-2 text-xs font-sans justify-between rounded-t-md h-9">makefile</div><div class="sticky top-9 md:top-[5.75rem]"><div class="absolute bottom-0 right-2 flex h-9 items-center"><div class="flex items-center rounded bg-token-main-surface-secondary px-2 font-sans text-xs text-token-text-secondary"><span class="" data-state="closed"><button class="flex gap-1 items-center py-1"><svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg" class="icon-sm"><path fill-rule="evenodd" clip-rule="evenodd" d="M7 5C7 3.34315 8.34315 2 10 2H19C20.6569 2 22 3.34315 22 5V14C22 15.6569 20.6569 17 19 17H17V19C17 20.6569 15.6569 22 14 22H5C3.34315 22 2 20.6569 2 19V10C2 8.34315 3.34315 7 5 7H7V5ZM9 7H14C15.6569 7 17 8.34315 17 10V15H19C19.5523 15 20 14.5523 20 14V5C20 4.44772 19.5523 4 19 4H10C9.44772 4 9 4.44772 9 5V7ZM5 9C4.44772 9 4 9.44772 4 10V19C4 19.5523 4.44772 20 5 20H14C14.5523 20 15 19.5523 15 19V10C15 9.44772 14.5523 9 14 9H5Z" fill="currentColor"></path></svg></button></span></div></div></div><div class="overflow-y-auto p-4" dir="ltr"><code class="!whitespace-pre hljs language-makefile"><span class="hljs-section">Authorization: Bearer &lt;seu-token-jwt&gt;</span>
</code></div></div></pre>
   </li>
</ol>
<h2>📄 Licença</h2>
<p>Este projeto está licenciado sob a licença MIT. Veja o arquivo <a rel="noopener" style="--streaming-animation-state: var(--batch-play-state-1); --animation-rate: var(--batch-play-rate-1);"><span style="--animation-count: 6; --streaming-animation-state: var(--batch-play-state-2);">LICENSE</span></a> para mais detalhes.</p>
<hr>