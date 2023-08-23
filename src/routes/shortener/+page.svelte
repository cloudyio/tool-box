<!-- Svelte Frontend -->
<script lang="ts">
    import { onMount } from 'svelte';
  
    let videoLink = '';
    let shortenedURL = '';
    let isLoading = false;
  
    async function shortenURL() {
      isLoading = true;
      try {
        const response = await fetch('http://localhost:5000/shorten', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json' // Set the Content-Type header to application/json
          },
          body: JSON.stringify({ long_url: videoLink }),
          mode: 'cors' // You can remove 'no-cors', use 'cors' to enable CORS
        });
  
        if (response.ok) {
          const data = await response.json();
          shortenedURL = data.short_url;
        } else {
          shortenedURL = `Error occurred. Status: ${response.status}`;
        }
      } catch (error) {
        console.error('Error:', error);
        shortenedURL = 'Error occurred. Please try again later.';
      } finally {
        isLoading = false;
      }
    }
  </script>
  
  <!-- Svelte Frontend - HTML -->
  <div class="h-screen flex justify-center items-center">
    <div class="bg-white dark:bg-slate-800 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl w-2/4 m-6">
      <h3 class="text-slate-900 dark:text-white text-lg font-medium mb-6">URL Shortener</h3>
  
      <form on:submit|preventDefault={shortenURL}>
        <div class="mb-4">
          <label for="videoLink" class="block text-slate-900 dark:text-white mb-2">Video Link</label>
          <input type="text" bind:value={videoLink} id="videoLink" name="videoLink" class="w-full px-3 py-2 border border-slate-300 rounded-md focus:outline-none focus:ring focus:ring-slate-200" placeholder="Input URL" required>
        </div>
  
        <button type="submit" class="w-full bg-indigo-500 hover:bg-indigo-600 text-white font-medium py-2 rounded-md">
          {#if isLoading}
            Loading...
          {:else}
            Submit
          {/if}
        </button>
      </form>
  
      {#if shortenedURL}
        <p class="mt-4">Shortened URL: <a href={shortenedURL} target="_blank" rel="noopener noreferrer">{shortenedURL}</a></p>
      {/if}
    </div>
  </div>
  