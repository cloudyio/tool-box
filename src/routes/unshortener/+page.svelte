<!-- Svelte Frontend -->
<script lang="ts">
    import { onMount } from 'svelte';
  
    let videoLink = '';
    let fullURL = '';
    let isLoading = false;
  
    async function extendURL() {
      isLoading = true;
      try {
        const response = await fetch('https://cloudys.tech/api/unshorten', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ url: videoLink }),
          
        });
  
        if (response.ok) {
          const data = await response.json();
          fullURL = data.url;
        } else {
          fullURL = `Error occurred. Status: ${response.status}`;
        }
      } catch (error) {
        console.error('Error:', error);
        fullURL = 'Error occurred. Please try again later.';
      } finally {
        isLoading = false;
      }
    }
  </script>
  
  <div class="h-screen flex justify-center items-center">
    <div class="bg-white dark:bg-slate-800 rounded-lg px-6 py-8 ring-1 ring-slate-900/5 shadow-xl w-2/4 m-6">
      <h3 class="text-slate-900 dark:text-white text-lg font-medium mb-6">URL Unshortener</h3>
  
      <form on:submit|preventDefault={extendURL}>
        <div class="mb-4">
          <label for="videoLink" class="block text-slate-900 dark:text-white mb-2">URL</label>
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
  
      {#if fullURL}
        <p class="mt-4">Full URL: <a href="{fullURL}" target="_blank" rel="noopener noreferrer" class="text-white">{fullURL}</a></p>
      {/if}
    </div>
  </div>
  